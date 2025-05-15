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
            print("this is the markdown")
            new_nodes.append(old_node)
            continue
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
        if rest:
            new_nodes.append(TextNode(rest, TextType.TEXT))
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
                # Text after the link working as expected

                # Todo check what happens when there is no text before the links
                # No text before link working as expected

                # Todo check what happens when there are multiple nodes
                # Multiple nodes working as expected
            

    for x in new_nodes:
        print(x)
    print('\n')
    return new_nodes      
            
            
# node = TextNode("text before the link [to royal](https://www.royal.com) text after the link", TextType.TEXT)
# link = split_nodes_link([node])

# node1 = TextNode("This node has three links [link one](https://www.google.com) number two [link two](https://www.images.com) number three [link three](https://www.linkthree.com)", TextType.TEXT)
# split_nodes_link([node1])

# !=======================================================================================
# Todo Finished this function and its tests, start working on the images function and its tests
def split_nodes_images(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        text = old_node.text
        
        alt_and_link = extract_markdown_images(text)
        if len(alt_and_link) == 0:
            new_nodes.append(old_node)
            continue
        for prop in alt_and_link:
            alt_image = prop[0]
            link = prop[1]
            markdown = f"![{alt_image}]({link})"
            
            while markdown in text:
                first_split = text.split(markdown, maxsplit=1)

                first_text = first_split[0]

                rest = first_split[1]

                if first_text:
                    new_nodes.append(TextNode(first_text, TextType.TEXT))
                new_nodes.append(TextNode(alt_image, TextType.IMAGE, link))
                text = rest
        if rest:
            new_nodes.append(TextNode(rest, TextType.TEXT))
                # Todo check what happens if there are no links

                # Todo check what happens when there is just one link

                # Todo check what happens when there are more than two links

                # Todo check what happens when there are no text between two links

                # Todo check what happens when theres just links and no text

                # Todo check what happens when there is text after the link

                # Todo check what happens when there is no text before the links

                # Todo check what happens when there are multiple nodes
            

    for x in new_nodes:
        print(x)
    print('\n')
    return new_nodes

node = TextNode("This is a text with an ![image](https://www.images.com) and a link [second](https://www.second.com)", TextType.TEXT)
yes = split_nodes_link([node])
no = split_nodes_images(yes)
# Todo in the second test suite, make sure to test for images, but also for a combination of images and links plus text...