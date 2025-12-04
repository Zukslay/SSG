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
            #raise Exception(f"delimiter->{delimiter} not found in text")
            new_list.append(node)
            continue
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
    
def split_nodes_image(old_nodes):
    new_list = []
    for node in old_nodes:
        text = node.text
        image_sec = extract_markdown_images(text)
        
        if not image_sec and text:
            new_list.append(node)
            continue
        final_text = True
        while image_sec:
            split_text = text.split(f"![{image_sec[0][0]}]({image_sec[0][1]})",1)
            new_list.append(TextNode(split_text[0], node.text_type))
            new_list.append(TextNode(image_sec[0][0], TextType.IMAGE, image_sec[0][1]))
            try:
                text = split_text[1]
            except IndexError:
                final_text = False
                break
            image_sec = extract_markdown_images(text)

        if final_text and text:
            new_list.append(TextNode(text, node.text_type))
    return new_list

def split_nodes_link(old_nodes):
    new_list = []
    for node in old_nodes:
        if node.text_type == TextType.IMAGE:
            new_list.append(node)
            continue
        text = node.text
        link_sec = extract_markdown_links(text)

        if not link_sec and text:
            new_list.append(node)
            continue
        final_text = True
        while link_sec:
            split_text = text.split(f"[{link_sec[0][0]}]({link_sec[0][1]})",1)
            new_list.append(TextNode(split_text[0], node.text_type))
            new_list.append(TextNode(link_sec[0][0], TextType.LINK, link_sec[0][1]))
            try:
                text = split_text[1]
            except IndexError:
                final_text = False
                break
            link_sec = extract_markdown_links(text)

        if final_text and text:
            new_list.append(TextNode(text, node.text_type))
    return new_list

def text_to_textnodes(text):
    node = TextNode(text, text_type=TextType.TEXT)
    nodes = split_nodes_image([node])
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes, "`", TextType.TEXT)
    nodes = split_nodes_delimiter(nodes, "**", TextType.TEXT)
    nodes = split_nodes_delimiter(nodes, "_", TextType.TEXT)
    return nodes



