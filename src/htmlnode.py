from enum import Enum
from textnode import TextNode, TextType

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if not self.props:
            return ""
        properties = list(map(lambda item: f'{item[0]}="{item[1]}"', self.props.items()))
        return " "+" ".join(properties)
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

class TagType(Enum):
    TEXT = "p"
    BOLD = "b"
    ITALIC = "i"
    LINK = "a"
    IMAGE = "img"
    CODE = "```"

class LeafNode(HTMLNode):

    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props=props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("invalid HTML: no value")
        if self.tag is None:
            return self.value
        if self.tag == "img":
            return f"<{self.tag}{self.props_to_html()} {self.value}/>"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children=children, props=props)  

    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode needs tag")
        if not self.children:
            raise ValueError("ParentNode needs children")
          
        t = self.tag
        html_list = [f"<{t}>"]
        for child in self.children:
            if isinstance(child, LeafNode):
                html_list.append(child.to_html())
            elif isinstance(child, ParentNode):
                html_list.append(child.to_html())
        return "".join(html_list) + f"</{t}>"
    
def text_node_to_html_node(node):
    if node.text_type == TextType.TEXT:
        return LeafNode(None,node.text)
    elif node.text_type == TextType.BOLD:
        return LeafNode("b", node.text)
    elif node.text_type == TextType.ITALIC:
        return LeafNode("i", node.text)
    elif node.text_type == TextType.LINK:
        return LeafNode('a', node.text, {"href": node.url})
    elif node.text_type == TextType.CODE:
        return LeafNode('code', node.text)
    elif node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": node.url, "alt": node.text})
    else:
        raise Exception("textnode type doesn't appear in TextType")
