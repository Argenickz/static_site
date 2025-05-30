import unittest
from _1_textnode import TextNode, TextType
from _7_split_images_and_links import split_nodes_link
# Todo check for empty spaces before/after links (make sure no nodes with empty spaces are being added to the list)
class LinkImageSplit(unittest.TestCase):
    def test_no_links(self):
        node = TextNode("This text has no links whatsoever", TextType.TEXT)
        link_node = split_nodes_link([node])
        self.assertEqual(
            [TextNode("This text has no links whatsoever", TextType.TEXT)],
            link_node
        )

    def test_one_link(self):
        node = TextNode("This node has one link [to youtube](https://www.youtube.com)", TextType.TEXT)
        link_node = split_nodes_link([node])
        self.assertEqual(
            [
                TextNode("This node has one link ", TextType.TEXT),
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com")
            ], 
            link_node
        )

    def test_three_links(self):
        node = TextNode("This node has three links [link one](https://www.google.com) number two [link two](https://www.images.com) number three [link three](https://www.linkthree.com)", TextType.TEXT)
        link_node = split_nodes_link([node])
        self.assertEqual(
            [
                TextNode("This node has three links ", TextType.TEXT),
                TextNode("link one", TextType.LINK, "https://www.google.com"),
                TextNode(" number two ", TextType.TEXT),
                TextNode("link two", TextType.LINK, "https://www.images.com"),
                TextNode(" number three ", TextType.TEXT),
                TextNode("link three", TextType.LINK, "https://www.linkthree.com")
            ],
            link_node
        )

    def test_no_text_between_links_with_text_at_beginning(self):
        node = TextNode("No text between two links [youtube](https://www.youtube.com)[google](https://www.google.com)", TextType.TEXT)
        link_node = split_nodes_link([node])
        self.assertEqual(
            [
                TextNode("No text between two links ", TextType.TEXT),
                TextNode("youtube", TextType.LINK, "https://www.youtube.com"),
                TextNode("google", TextType.LINK, "https://www.google.com")

            ],
            link_node
        )

    def test_just_links(self):
        node = TextNode("[to apple](https://www.apple.com)[to amazon](https://www.amazon.com)", TextType.TEXT)
        link_node = split_nodes_link([node])
        self.assertEqual(
            [
                TextNode("to apple", TextType.LINK, "https://www.apple.com"),
                TextNode("to amazon", TextType.LINK, "https://www.amazon.com")
            ],
            link_node
        )

    def test_text_after_link(self):
        node = TextNode("text before the link [to royal](https://www.royal.com) text after the link", TextType.TEXT)
        link_node = split_nodes_link([node])
        self.assertEqual(
            [
                TextNode("text before the link ", TextType.TEXT),
                TextNode("to royal", TextType.LINK, "https://www.royal.com"),
                TextNode(" text after the link", TextType.TEXT)
            ],
            link_node
        )

    def test_no_text_before_link(self):
        node = TextNode("[to hi 5](https://www.hi5.com) also this", TextType.TEXT)
        link_node = split_nodes_link([node])
        self.assertEqual(
            [
                TextNode("to hi 5", TextType.LINK, "https://www.hi5.com"),
                TextNode(" also this", TextType.TEXT)
            ],
            link_node
        )
    
    def test_multiple_nodes(self):
        node1 = TextNode("this is the first [to samsung](https://www.samsung.com)", TextType.TEXT)
        node2 = TextNode("this is the second [to android](https://www.android.com)", TextType.TEXT)
        link_node = split_nodes_link([node1, node2])
        self.assertEqual(
            [
                TextNode("this is the first ", TextType.TEXT),
                TextNode("to samsung", TextType.LINK, "https://www.samsung.com"),
                TextNode("this is the second ", TextType.TEXT),
                TextNode("to android", TextType.LINK, "https://www.android.com")
            ],
            link_node
        )
    
    def test_different_text_type(self):
        node = TextNode("this node has a bold text type", TextType.BOLD)
        link = split_nodes_link([node])
        self.assertEqual(
            [
                TextNode("this node has a bold text type", TextType.BOLD)
            ],
            link
        )

    def test_empty_space_before_and_after_link(self):
        node = TextNode("   [image](https://www.images.com)   ", TextType.TEXT)
        link_node = split_nodes_link([node])
        self.assertEqual(
            [
                TextNode("image", TextType.LINK, "https://www.images.com")
            ],
            link_node
        )


if __name__ == "__main__":
    unittest.main()