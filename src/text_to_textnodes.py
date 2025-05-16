from textnode import TextNode, TextType
from delimiter import split_nodes_delimiter
from split_images_and_links import split_nodes_images, split_nodes_link
# ! Text to TextNodes

# Tome to put al the 'splitting' functions together into a function that can convert a raw string of markdown-flavored text into a list of TextNode objects.

# 1. Create 'text_to_textnodes(text) function. Here's some example input:
# ` This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)

# It should output this list of nodes:

# [
#     TextNode("This is ", TextType.TEXT),
#     TextNode("text", TextType.BOLD),
#     TextNode(" with an ", TextType.TEXT),
#     TextNode("italic", TextType.ITALIC),
#     TextNode(" word and a ", TextType.TEXT),
#     TextNode("code block", TextType.CODE),
#     TextNode(" and an ", TextType.TEXT),
#     TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
#     TextNode(" and a ", TextType.TEXT),
#     TextNode("link", TextType.LINK, "https://boot.dev"),
# ]

raw = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"


# Todo, This works, will summit and run tests tomorrow, push.
def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)
    node = split_nodes_delimiter([node], "**", TextType.BOLD)
    node = split_nodes_delimiter(node, "_", TextType.ITALIC)
    node = split_nodes_delimiter(node, "`", TextType.CODE)
    node = split_nodes_link(node)
    node = split_nodes_images(node)


   
    return node

test = text_to_textnodes(raw)
for x in test:
    print(x)