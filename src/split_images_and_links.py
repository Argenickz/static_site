from textnode import TextNode, TextType
from link_image_extractor import extract_markdown_images, extract_markdown_links
# ! Split Images and Links
# Now that we have the extraction functions, we will need to be able to split raw markdown into TextNodes based on images and links.

# Assignment
# 1. Create two new functions:
# def split_nodes_image(old_nodes):
# def split_nides_link(old_node):

# They should behave very similar to 'split_nodes_delimiter', but obviously don't need a delimiter or a text type as input, because they always operate on images or links respectively. Here's some example usage:

# node = TextNode(
#     "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
#     TextType.TEXT,
# )
# new_nodes = split_nodes_link([node])
# [
#     TextNode("This is text with a link ", TextType.TEXT),
#     TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
#     TextNode(" and ", TextType.TEXT),
#     TextNode(
#         "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
#     ),
# ]



def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        text = old_node.text
        
        alt_and_link = extract_markdown_links(text)
        if len(alt_and_link) == 0:
            new_nodes.append(old_node)
        for prop in alt_and_link:
            alt_text = prop[0]
            link = prop[1]
            markdown = f"[{alt_text}]({link})"
            
            while markdown in text:
                first_split = text.split(markdown, maxsplit=1)

                first_text = first_split[0]

                rest = first_split[1]

                if first_text:
                    new_nodes.append(TextNode(first_text, TextType.TEXT))
                new_nodes.append(TextNode(alt_text, TextType.LINK, link))
                text = rest
                # Todo check what happens if there are no links
                # IF there are no links just add the TextNode as is to the list (Done)

                # Todo check what happens when there is just one link
                # One link working as expected (Done)

                # Todo check what happens when there are more than two links
                # Multiple links working as expected (Done)

                # Todo check what happens when there are no text between two links
                # No text workinf as expected (Done)

                # Todo check what happens when theres just links and no text
                # Just links and no text working as expected (Done)

                # Todo check what happens when there is text after the link
                # Text after the link not being added

                # Todo check what happens when there is no text before the links

                # Todo check what happens when there are multiple nodes
            

    for x in new_nodes:
        print(x)
    print('\n')
    return new_nodes      
            
            
            
# # Two links and text
# node1 = TextNode(
#     "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
#     TextType.TEXT,
# )

# # No links
# node2 = TextNode("This text has no links whatsoever", TextType.TEXT)

# split_nodes_link([node1])
# split_nodes_link([node2])

# Todo Continue tests tomorrow... git push

