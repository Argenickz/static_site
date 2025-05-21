from _1_textnode import TextNode, TextType
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
    new_nodes = []
    # Run a loop for the nodes in the list
    for old_node in old_nodes:
        # If the node type is not a text type just add it to the list as is and skip this iteration

        if old_node.text_type == TextType.TEXT and delimiter not in old_node.text:
            new_nodes.append(old_node)
            continue
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        # Assign the text of an old node into a variable
        text = old_node.text
        # Don't add any text nodes which text is None or the delimiter is not in the text
        if delimiter not in text:
            continue

        # Run a while loop with the delimiter as a conditional
        while delimiter in text:
            # Get the first split as a list
            first_split = text.split(delimiter, maxsplit=1)
            # print(f"this is the first split {first_split}")
            # Get the value of the first text
            first_text = first_split[0]
            # Assign the second part of the text to a variable to check if the delimiter exists in it, if not raise an exception
            second_text = first_split[1]
            if delimiter not in second_text:
                raise Exception("Invalid markdown, no matching closing delimiter")
            # Get the value of the second split
            second_split = second_text.split(delimiter, maxsplit=1)
            # Get the value of the markdown word
            markdonw = second_split[0]
            # Assign the second split as the rest of the text
            rest = second_split[1]
            # Check if the first text is not empty, if not then add it to the nodes list as a TextNode
            if first_text:
                new_nodes.append(TextNode(first_text, TextType.TEXT))
            # Add the markdown words with its appropriate text type
            new_nodes.append(TextNode(markdonw, text_type))
            # assign the test as the rest
            text = rest

        # Check this condition outside of the loop to see if there's more text at the rest
        if rest:
            new_nodes.append(TextNode(rest, TextType.TEXT))

    
    return new_nodes


# =======================================================================================








