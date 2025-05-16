import unittest
from textnode import TextNode, TextType
from delimiter import split_nodes_delimiter
class TestDelimiter(unittest.TestCase):
    def test_simple_delimiter(self):
        node = TextNode("This is some text with a **bolded** word", TextType.TEXT)
        new_node = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            [
                TextNode("This is some text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT)
            ],
            new_node
        )
    
    def test_delim_at_the_end(self):
        node = TextNode("The bolded word is **here**", TextType.TEXT)
        new_node = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            [
                TextNode("The bolded word is ", TextType.TEXT),
                TextNode("here", TextType.BOLD)
            ],
            new_node
        )

    def test_delim_at_beginning(self):
        node = TextNode("**This** is what you're looking for", TextType.TEXT)
        new_node = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            [
                TextNode("This", TextType.BOLD),
                TextNode(" is what you're looking for", TextType.TEXT)
            ],
            new_node
        )

    def test_multiple_delimiters(self):
        node1 = TextNode("Don't believe **everything** you see", TextType.TEXT)
        node2 = TextNode("If it's too good to be **true**", TextType.TEXT)
        new_node = split_nodes_delimiter([node1, node2], "**", TextType.BOLD)
        self.assertEqual(
            [
                TextNode("Don't believe ", TextType.TEXT),
                TextNode("everything", TextType.BOLD),
                TextNode(" you see", TextType.TEXT),
                TextNode("If it's too good to be ", TextType.TEXT),
                TextNode("true", TextType.BOLD)
            ],
            new_node
        )

    def test_different_delimiters(self):
        node = TextNode("_This is italic_ and **this is bolded** also `this is code` of course", TextType.TEXT)
        new_node = split_nodes_delimiter([node], "_", TextType.ITALIC)
        new_node = split_nodes_delimiter(new_node, "**", TextType.BOLD)
        new_node = split_nodes_delimiter(new_node, "`", TextType.CODE)
        self.assertEqual(
            [
                TextNode("This is italic", TextType.ITALIC),
                TextNode(" and ", TextType.TEXT),
                TextNode("this is bolded", TextType.BOLD),
                TextNode(" also ", TextType.TEXT),
                TextNode("this is code", TextType.CODE),
                TextNode(" of course", TextType.TEXT)
            ],
            new_node
        )






if __name__ == "__main__":
    unittest.main()