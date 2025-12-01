import unittest
from htmlnode import LeafNode, TagType



class TestLeafNode(unittest.TestCase):
    def test1(self):
        node1 = LeafNode("p", "Hello, world!")
        self.assertEqual(node1.to_html(), "<p>Hello, world!</p>")
    def test2(self):
        node2 = LeafNode("img", "", props={"src": "imagesource","alt": "lolo"})
        self.assertEqual(node2.to_html(), '<img src="imagesource" alt="lolo" />')

    def test3(self):
        node3 = LeafNode("a", "click me", {"href": "www.facebook.com"})
        self.assertEqual(node3.to_html(), '<a href="www.facebook.com">click me</a>')
    
    