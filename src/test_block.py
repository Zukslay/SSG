import unittest
from functions_block import markdown_to_blocks, block_to_block_type, BlockType,markdown_to_html_node

class testBLOCK(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    def test_block_to_block_type(self):
        md = """
### I'm a heading  

# I'm invisible   

``` if 1 - 1 == False: return "you are smart!!(sarcasm)" ```

>this is a quote

>>a quotequote?

- this is an unordered list item
- another unordered list item in the same list
- another
- and another
- and another
- and another
- and another
- another
- ...
- ...
- serious?
- you have no business?

This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

1. I'm the number one
2. I'm nobody
3. I'm third
4. I'm a NPC
"""
        blocks = markdown_to_blocks(md)
        types = []
        for block in blocks:
            types.append(block_to_block_type(block))

        self.assertListEqual(
            types,
            [
                BlockType.HEADING,
                BlockType.HEADING,
                BlockType.CODE,
                BlockType.QUOTE,
                BlockType.QUOTE,
                BlockType.UNORDERED_LIST,
                BlockType.PARAGRAPH,
                BlockType.PARAGRAPH,
                BlockType.ORDERED_LIST
                
            ]
        )
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
        html,
        "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
    )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
        html,
        "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
    )
    def test_simple_heading(self):
        md = "# Hello **world**"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html,
            "<div><h1>Hello <b>world</b></h1></div>")
        
    def test_simple_heading(self):
        md = "> a _quoted_ **line**"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html,
            "<div><blockquote>a <i>quoted</i> <b>line</b></blockquote></div>")
        
    def test_simple_heading(self):
        md = "- one\n- two with `code`"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html,
            "<div><ul><li>one</li><li>two with <code>code</code></li></ul></div>")
        
    def test_simple_heading(self):
        md = "1. first\n2. second **bold**"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html,
            "<div><ol><li>first</li><li>second <b>bold</b></li></ol></div>")
        
    def test_simple_heading(self):
        md = """
# Title

> quoted _text_

- item **one**
- item two
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html,
            "<div><h1>Title</h1><blockquote>quoted <i>text</i></blockquote><ul><li>item <b>one</b></li><li>item two</li></ul></div>"
)


