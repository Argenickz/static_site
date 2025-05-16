import unittest

from textnode import TextNode, TextType
from split_images_and_links import split_nodes_images, split_nodes_link


class TesttLinkAndImageNode(unittest.TestCase):
    def test_no_links(self):
        node = TextNode("This text has no links", TextType.TEXT)
        image_node = split_nodes_images([node])
        self.assertEqual(
            [
                TextNode("This text has no links", TextType.TEXT)
            ],
            image_node
        )

    def test_one_link(self):
        node = TextNode("Here's that image you asked for ![image](https://www.images.com)", TextType.TEXT)
        image_node = split_nodes_images([node])
        self.assertEqual(
            [
                TextNode("Here's that image you asked for ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://www.images.com")
            ],
            image_node
        )

    def test_three_links(self):
        node = TextNode("first image ![pluto](https://www.planets.com) second image ![a car](https://www.tesla.com) third image ![just a hat](https://www.hats.com)", TextType.TEXT)
        image_node = split_nodes_images([node])
        self.assertEqual(
            [
                TextNode("first image ", TextType.TEXT),
                TextNode("pluto", TextType.IMAGE, "https://www.planets.com"),
                TextNode(" second image ", TextType.TEXT),
                TextNode("a car", TextType.IMAGE, "https://www.tesla.com"),
                TextNode(" third image ", TextType.TEXT),
                TextNode("just a hat", TextType.IMAGE, "https://www.hats.com")
            ],
            image_node
        )

    def test_no_text_between_links_with_text_at_beginning(self):
        node = TextNode("![one coke](https://www.coke.com)![airpods](https://www.airpods.com) dramatic effect", TextType.TEXT)
        link_node = split_nodes_images([node])
        self.assertEqual(
            [
                TextNode("one coke", TextType.IMAGE, "https://www.coke.com"),
                TextNode("airpods", TextType.IMAGE, "https://www.airpods.com"),
                TextNode(" dramatic effect", TextType.TEXT)
            ],
            link_node
        )

    def test_just_links(self):
        node = TextNode("![link one](https://www.justdoit.com)![link two](https://www.maybelater.com)", TextType.TEXT)
        link_node = split_nodes_images([node])
        self.assertEqual(
            [
                TextNode("link one", TextType.IMAGE, "https://www.justdoit.com"),
                TextNode("link two", TextType.IMAGE, "https://www.maybelater.com")
            ],
            link_node
        )

    def test_no_text_before_link(self):
        node = TextNode("![to hi 5](https://www.hi5.com) also this", TextType.TEXT)
        link_node = split_nodes_images([node])
        self.assertEqual(
            [
                TextNode("to hi 5", TextType.IMAGE, "https://www.hi5.com"),
                TextNode(" also this", TextType.TEXT)
            ],
            link_node
        )
    
    def test_multiple_nodes(self):
        node1 = TextNode("this is the first ![to samsung](https://www.samsung.com)", TextType.TEXT)
        node2 = TextNode("this is the second ![to android](https://www.android.com)", TextType.TEXT)
        link_node = split_nodes_images([node1, node2])
        self.assertEqual(
            [
                TextNode("this is the first ", TextType.TEXT),
                TextNode("to samsung", TextType.IMAGE, "https://www.samsung.com"),
                TextNode("this is the second ", TextType.TEXT),
                TextNode("to android", TextType.IMAGE, "https://www.android.com")
            ],
            link_node
        )
    
    def test_different_text_type(self):
        node = TextNode("this node has a bold text type", TextType.BOLD)
        link = split_nodes_images([node])
        self.assertEqual(
            [
                TextNode("this node has a bold text type", TextType.BOLD)
            ],
            link
        )

    def test_empty_space_before_and_after_link(self):
        node = TextNode("   ![image](https://www.images.com)   ", TextType.TEXT)
        link_node = split_nodes_images([node])
        self.assertEqual(
            [
                TextNode("image", TextType.IMAGE, "https://www.images.com")
            ],
            link_node
        )

    def test_link_and_images(self):
        node = TextNode("this node has an image ![a running shoe](https://www.nike.com) it also has a link [shopping cart](https://www.checkout.com) some fancy letters    ", TextType.TEXT)
        link_node = split_nodes_link([node])
        link_node = split_nodes_images(link_node)
        self.assertEqual(
            [
                TextNode("this node has an image ", TextType.TEXT),
                TextNode("a running shoe", TextType.IMAGE, "https://www.nike.com"),
                TextNode(" it also has a link ", TextType.TEXT),
                TextNode("shopping cart", TextType.LINK, "https://www.checkout.com"),
                TextNode(" some fancy letters    ", TextType.TEXT)
            ],
            link_node
        )

if __name__ == "__main__":
    unittest.main()