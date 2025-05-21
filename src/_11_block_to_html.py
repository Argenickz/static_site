from _1_textnode import TextNode, TextType, text_node_to_html_node
from _8_text_to_textnodes import text_to_textnodes
from _9_split_blocks import markdown_to_blocks
from _10_block_type import block_to_block_type
from pprint import pprint
"""
! Block to HTML

!Assignment
Create a new function called 'def markdown_to_html_node(markdown):' That converts a full markdown document into a single parent HTMLNode. That one parent HTMLNode should obviously contain many child HTMLNode objects representing the nested elements.

FYI: I created an additional 8 helper functions to keep my code neat and easy to understand, because there's a lot of logic necessary for 'markdown_to_html_node' I don't want to give you the exact functions because I want you to do this from scratch. However, I'll give you the basic order of operations:

1. Split the markdown into blocks (you already have a function for this)

2. Loop over each block:
    1. Determine the type of block (you already have a function for this)

    2. Based on the type of block, create a new HTMLNode with the proper data

    3. Assign the proper child HTMLNode object to the block node. I created a shared 'text_to_children(text)' function that works for all block types. It takes a string of text and returns a list of HTMLNodes that represent the inline markdown using previously created functions (think TextNode --> HTMLNode).

    4. The 'code' block is a bit of a special case: It should   NOT do any inline markdown parsing of its children. I didn't use my 'text_to_children function for this block type, I manually made a TextNode and used 'text_node_to_html_node. 

3. Make all the block nodes children under a single parent HTML node (which should just be a div) and return it.

4. Create unit tests (Look at the unit test for an idea of the actual outcome.)
"""
# def test_paragraphs(self):
#     md = """
# This is **bolded** paragraph
# text in a p
# tag here

# This is another paragraph with _italic_ text and `code` here

# """

#     node = markdown_to_html_node(md)
#     html = node.to_html()
#     self.assertEqual(
#         html,
#         "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
#     )

# def test_codeblock(self):
#     md = """
# ```
# This is text that _should_ remain
# the **same** even with inline stuff
# ```
# """

#     node = markdown_to_html_node(md)
#     html = node.to_html()
#     self.assertEqual(
#         html,
#         "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
#     )

# Todo this is just a test run to make sure I understand the logic, once I get it down, we're going to be writing additional helper functions to make the code more readable and concise.
def markdown_to_html_node(markdown):
    # Split the markdown into blocks (split_blocks)
    markdown_blocks = markdown_to_blocks(markdown)
    # Loop over each block

    node_list = []
    for block in markdown_blocks:

        # Determine the type of block (block_type)
        block_type = block_to_block_type(block)

        # Check if the code block is a paragraph
        if block_type.PARAGRAPH:
            # Use text_to_textnodes to create textnodes with their respective data type
            node_list.extend(text_to_textnodes(block))
            
    
    pprint(node_list)
    for x in node_list:
        print(text_node_to_html_node(x).to_html())
    # Todo, So far this returns a list of text nodes with their respective text and text type. I need to figure out a way of making this into an actual child node, and add it to a parent (div) node, but tomorrow, cause it's too late... maybe textnode_to_html?   run this and take a look at the outcome, this just need a p tag and a div (parentnode) keep on refining tomorrow.
        







#! This
markdown = """
This is a **bolded** paragraph
text with a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
markdown_to_html_node(markdown)

#! Should output this
result =   """
<div><p>This is <b>bolded</b> paragraph text in a p tag here</p>
<p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>"""


# ! Create helper functions here for simplicity.1



