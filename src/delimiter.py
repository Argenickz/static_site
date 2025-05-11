from textnode import TextNode, TextType
#! Split Delimiter
# Now that we can convert TextNodes to HTMLNodes, we need to be able to create TextNodes from raw markdown strings. For example, the string:
# "This is text with a **bolded phrase** in the middle"
# Should become:
# [
#     TextNode("This is text with a ", TextType.TEXT),
#     TextNode("bolded phrase", TextType.BOLD),
#     TextNode(" in the middle", TextType.TEXT),
# ]

# 1. Create a function 'split_nodes_delimiter(old_nodes, delimiter, text_type), It takes a list of old nodes, a delimiter and a text type. It should return a new list of nodes, where any 'text' type nodes in the input list are (potentially) split into multiple nodes based on the syntax. For example, given the following 
#`` node = TextNode("This is text with a `code block` word", TextType.TEXT)
#`` new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
# Should become:
#`` [
#``     TextNode("This is text with a ", TextType.TEXT),
#``     TextNode("code block", TextType.CODE),
#``     TextNode(" word", TextType.TEXT),
#`` ]
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    # Create a list to get a hold of the new nodes
    for old_node in old_nodes:
        print(old_node.text)





test = TextNode("this is a text with a **bolded** word in the middle", TextType.TEXT)
split_nodes_delimiter([test], "**", TextType.BOLD)
# 2. Write a bunch of texts for this one, specially tests where there are multiple types of delimiters in the text.