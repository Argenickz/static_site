import unittest
from _4_parentnode import ParentNode
from _3_leafnode import LeafNode

class Test_ParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>"
        )

    def test_links(self):
        child_node = LeafNode("a", "the good stuff", {"href": "https://www.good.com"})
        parent_node = ParentNode(
            "div", [child_node], {"target": "https://www.testing.com"})
        self.assertEqual(
            parent_node.to_html(),
            '<div target="https://www.testing.com"><a href="https://www.good.com">the good stuff</a></div>'
        )
if __name__ == "__main__":
    unittest.main()