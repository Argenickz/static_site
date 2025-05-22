# This is where we'll run our tests for the TextNode class.

import unittest
from _1_textnode import TextNode, TextType, text_node_to_html_node



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
        

class TestTextToHtmlNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_node_with_link(self):
        node = TextNode("click me!", TextType.LINK, "https://www.myproject.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(
            html_node.to_html(),
            '<a href="https://www.myproject.com">click me!</a>'
        )
        self.assertEqual(html_node.tag, 'a')
        self.assertEqual(html_node.props, {"href": "https://www.myproject.com"})
        

if __name__ == "__main__":
    unittest.main()