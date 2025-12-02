import unittest

from textnode import TextNode, TextType
from functions import split_nodes_delimiter, extract_markdown_images,extract_markdown_links


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node2", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )
    
    def test_delimiter(self):
        node = TextNode("this is a text with `code``code1` and no more", TextType.TEXT)
        nodes1 = split_nodes_delimiter([node], "`", TextType.TEXT)
        nodes2 = [
            TextNode("this is a text with ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode("code1", TextType.CODE),
            TextNode(" and no more", TextType.TEXT)
        ]
        for n1,n2 in zip(nodes1,nodes2):
            self.assertEqual(n1, n2)
    
    def test_extract_images(self):
        matches = extract_markdown_images(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
    )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_link(self):
        matches = extract_markdown_links(
        "[as](http://i.k.z/as) [aa](https://outlook.com) ![as](asdad)"
    )
        self.assertListEqual(
            [("as", "http://i.k.z/as"),
             ("aa","https://outlook.com")
             ],
             matches
        )

if __name__ == "__main__":
    unittest.main()