from enum import Enum
from htmlnode import HTMLNode, ParentNode, text_node_to_html_node, LeafNode
from functions_inline import text_to_textnodes
import re

class BlockType(Enum):
    PARAGRAPH = "p"
    HEADING = "h"
    CODE = "code"
    QUOTE = "blockquote"
    UNORDERED_LIST = "ul"
    ORDERED_LIST = "ol"

def markdown_to_blocks(text):
    j = text.strip()
    j = j.strip("\n")
    new_list = list(map(lambda x: x.strip(), j.split("\n\n")))
    final_list = []
    for k in new_list:
        if k.strip():
            final_list.append(k)
    return final_list

def block_to_block_type(blocky):
    block = blocky.strip()
    
    if bool(re.match(r"^#{1,6} ", block)):
        return BlockType.HEADING
    elif bool(re.match(r"^```",block)) and bool(re.search(r"```\s*$", block)):
        return BlockType.CODE
    elif bool(re.match(r"^>", block)):
        return BlockType.QUOTE
    
    condition_unord = True
    for line in block.split("\n"):
        if not bool(re.match(r"^- ",line)):
            condition_unord = False
            break
    if condition_unord:
        return BlockType.UNORDERED_LIST
    
    condition_ord = True
    for a,line in enumerate(block.split("\n")):
        if not re.match(rf"^{a+1}\. ", line):
            condition_ord = False
            break
    if condition_ord:
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
    
def count_hashes(text):
    match = re.match(r"^(#{1,6}) ", text)
    if match:
        return len(match.group(1))
    return None

def text_to_children(text):
    new_list = []
    nodes = text_to_textnodes(text)
    for node in nodes:
        new_list.append(text_node_to_html_node(node))
    return new_list
    
def cleaner(text, type):
    if type == BlockType.HEADING:
        return re.sub(r"^#{1,6} ", "", text)
    
    elif type == BlockType.CODE:
        lines = text.split("\n")[1:-1]
        return "\n".join(lines) + "\n"
        
    
    elif type == BlockType.QUOTE:
        lines = text.split('\n')
        strip_list = []
        for line in lines:
            strip_list.append(re.sub(r"^> ", "", line))
        return "\n".join(strip_list)

    elif type == BlockType.PARAGRAPH:
        return " ".join(text.split("\n"))

    elif type == BlockType.ORDERED_LIST:
        lines = text.split("\n")
        strip_list = []
        for line in lines:
            strip_list.append(re.sub(r"^\d+\. ", "", line))
        return "\n".join(strip_list)
    
    elif type == BlockType.UNORDERED_LIST:
        lines = text.split("\n")
        strip_list = []
        for line in lines:
            strip_list.append(re.sub(r"^[*-] ", "", line))
        return "\n".join(strip_list)

    else:
        raise Exception("type not supported")
    
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        clean_block = cleaner(block, block_type)
        
        if block_type == BlockType.HEADING:
            a = count_hashes(block)
            childs = text_to_children(clean_block)
            htmlnod = ParentNode(f"h{a}", children=childs)
        
        elif block_type == BlockType.CODE:
            child = LeafNode("code",clean_block)
            htmlnod = ParentNode("pre",children=[child])
        
        elif block_type == BlockType.PARAGRAPH:
            childs = text_to_children(clean_block)
            htmlnod = ParentNode("p", children=childs)

        elif block_type == BlockType.QUOTE:
            childs = text_to_children(clean_block)
            htmlnod = ParentNode("blockquote", children=childs)

        elif block_type == BlockType.UNORDERED_LIST:
            block_childs = []
            for line in clean_block.split("\n"):
                if not line.strip():
                    continue

                childs = text_to_children(line)
                block_childs.append(ParentNode("li", children=childs))
            htmlnod = ParentNode("ul", children=block_childs)

        elif block_type == BlockType.ORDERED_LIST:
            block_childs = []
            for line in clean_block.split("\n"):
                if not line.strip():
                    continue

                childs = text_to_children(line)
                block_childs.append(ParentNode("li", children=childs))
            htmlnod = ParentNode("ol", children=block_childs)
        
        html_nodes.append(htmlnod)
        
    return ParentNode("div",children=html_nodes)
    
def converter(md):
    node = markdown_to_html_node(md)
    return node.to_html()
