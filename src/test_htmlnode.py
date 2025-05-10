import unittest
from htmlnode import HTMLNode
class TestHTMLNode(unittest.TestCase):

    def test_same_nodes(self):
        node1 = HTMLNode("p", "simple test", None, {"href": "https://www.simpletest.com"})
        node2 = HTMLNode("a", "simple test", None, {"href": "https://www.different.com"})
        self.assertEqual(node1.tag, 'p')
        self.assertEqual(node1.props_to_html(), ' href="https://www.simpletest.com"')
        self.assertEqual(node1.children, None)
        self.assertNotEqual(node1.tag, node2.tag)
        self.assertNotEqual(node1.props_to_html(), node2.props_to_html())

    def test_no_props(self):
        node = HTMLNode("p", "a test", None, None)
        self.assertEqual(node.value, 'a test')
        self.assertEqual(node.children, None)
        self.assertEqual(node.props_to_html(), '')
        self.assertNotEqual(node.props_to_html(), ('None'))



if __name__ == "__main__":
    unittest.main()