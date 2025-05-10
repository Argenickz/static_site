import unittest
from leafnode import LeafNode
class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html(self):
        node = LeafNode("p", "random text")
        self.assertEqual(node.to_html(), "<p>random text</p>")

    def test_link(self):
        node = LeafNode("a", "click me", {"href": "https://www.itsascam.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.itsascam.com">click me</a>'
        )
    
    def test_multiple_links(self):
        node = LeafNode("a", "this is unexpected!", {"href": "https://www.gotcha.com", "target": "https://www.testing.com"})

        self.assertEqual(
            node.to_html(),
            '<a href="https://www.gotcha.com" target="https://www.testing.com">this is unexpected!</a>'
        )

if __name__ == "__main__":
    unittest.main()