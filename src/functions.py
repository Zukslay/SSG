from textnode import TextType, TextNode
import re

types = {
    "`": TextType.CODE,
    "**": TextType.BOLD,
    "_": TextType.ITALIC
}

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_list = []
    if delimiter not in types:
        raise Exception(f"delimiter->{delimiter} not supported")
    for node in old_nodes:
        if not node.text_type == text_type:
            new_list.append(node)
            continue
        if delimiter not in node.text:
            raise Exception(f"delimiter->{delimiter} not found in text")
        if node.text.count(delimiter) % 2 != 0:
            raise Exception(f"delimiter not closed")
        
        for a,text in enumerate(node.text.split(delimiter)):
            if text and a % 2 == 0:
                new_list.append(TextNode(text, TextType.TEXT))
            elif text and a % 2 == 1:
                new_list.append(TextNode(text, types[delimiter]))
    
    return new_list

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)",text)


