import unittest
from functions_block import markdown_to_blocks, block_to_block_type, BlockType

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