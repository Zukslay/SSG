from functions_block import markdown_to_html_node, text_to_children, cleaner, markdown_to_blocks
from htmlnode import HTMLNode

def testp(md):
    node = markdown_to_html_node(md)
    html = node.to_html()
    return html

test = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
#print("====================================")
print(testp(test))

#print("====================================")
#print("<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>")


