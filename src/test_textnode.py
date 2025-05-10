# This is where we'll run our tests for the TextNode class.

import unittest

from textnode import TextNode, TextType

# Todo Write more cases
class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is something", TextType.ITALIC)
        node2 = TextNode("This is something else", TextType.TEXT)
        self.assertNotEqual(node, node2)
        self.assertNotEqual(node.text_type, node2.text_type)
        self.assertEqual(node.url, None)

    def test_types(self):
        bold = TextNode("Bold Text", TextType.BOLD)
        italic = TextNode("Italic Text", TextType.ITALIC)
        self.assertNotEqual(bold.text_type, italic.text_type)
        
if __name__ == "__main__":
    unittest.main()