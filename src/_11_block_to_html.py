from _1_textnode import TextNode, TextType, text_node_to_html_node
from _4_parentnode import ParentNode
from text_to_textnodes import text_to_textnodes
from _9_split_blocks import markdown_to_blocks
from _10_block_type import block_to_block_type, BlockType
from pprint import pprint
from _3_leafnode import LeafNode
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


def markdown_to_html_node(markdown):
    """paragraphs start and end with (tripe quotes)
    every item in an ordered list starts with (1. and so on)
    every item in an unordered list starts with (- and so on)
    headings can start with one # or more, up so 6 #
    code starts with ``` and ends with ```
    quotes start with > for every line
    """
    # Split the markdown into blocks (split_blocks)
    markdown_blocks = markdown_to_blocks(markdown)
    # print(f'this is the markdown blocks{markdown_blocks}')
    node_list = []

    # Loop over each block
    for block in markdown_blocks:
        
        
        # Determine the type of block (block_type)
        block_type = block_to_block_type(block)
        

        # Check if the code block is a paragraph
        if block_type == BlockType.PARAGRAPH:
            # adds the children returned by this function to the list
            node_list.append(paragraph_to_html(block))

        # Todo. Fixed unordered list to correctly parse different types of nodes inside the list items.
        if block_type == BlockType.UNORDERED_LIST:
            node_list.append(unordered_list_to_html(block))
        
        if block_type == BlockType.ORDERED_LIST:
            node_list.append(ordered_list_to_html(block))

        if block_type == BlockType.QUOTE:
            node_list.append(quote_to_html(block))

        if block_type == BlockType.CODE:
            node_list.append(code_to_html(block))

        if block_type == BlockType.HEADING:
            node_list.extend(headings_to_html(block))
    
    # Returns the children in the list under a single 'div' tag
    # print(f'\n\n this is the node list:\n\n{node_list}')
    return ParentNode("div", node_list)
    return node_list




# ====================================================================================
            
def paragraph_to_html(block):
    children = text_to_textnodes(block.replace("\n", " "))
    child_list = [text_node_to_html_node(son) for son in children]
    return ParentNode("p", child_list)

# =======================================================================================
# Todo Separate unordered and ordered list for simplicity
def unordered_list_to_html(block):
    blocks = block.split("\n")

    text_nodes = [text_to_textnodes(text.lstrip("- ")) for text in blocks]
    html_nodes = list(map(lambda sublist: list(map(lambda node: text_node_to_html_node(node), sublist)), text_nodes))
    children = list(map(lambda node: ParentNode("li", node), html_nodes))
    return ParentNode("ul", children)
# =======================================================================================
def ordered_list_to_html(block):
    # the ordered list is not supposed to have the number and space passed in the markdown string. so '1. this' becomes: '<li>this</li>
    blocks = block.split("\n")
    stripped_blocks = []
    # Use a range to delete the number and space from each item in the list
    for index in range(len(blocks)):
        stripped_blocks.append(blocks[index].strip(f"{index + 1}. "))
    text_nodes = [text_to_textnodes(text) for text in stripped_blocks]
    html_nodes = list(map(lambda sublist: list(map(lambda node: text_node_to_html_node(node), sublist)), text_nodes))
    children = list(map(lambda node: ParentNode("li", node), html_nodes))
    return ParentNode("ol", children)        

# =======================================================================================

def quote_to_html(block):
    text_nodes = []
    # print(block)
    blocks = block.split("\n")
    # This list comprehension here adds a space at the end of every sentence but the last one to have spaces between.
    spaced = [string + ' ' if len(blocks) != blocks.index(string) + 1 else string for string in blocks]
    # print(blocks, '\n')
    for text in spaced:
        text_nodes.extend(text_to_textnodes(text.lstrip("> ")))
    # print(f"text node list: \n{text_nodes}\n")
    html_nodes = [text_node_to_html_node(item) for item in text_nodes]
    # print(f"this is the html list\n{html_nodes}")
    return ParentNode("blockquote", html_nodes)  

# =======================================================================================

def code_to_html(block):
    # Using replace() with a count argument, like 1, will only replace the first instance of a character
    blocks = block.lstrip("```").rstrip("```").replace("\n", "", 1)
    blocks = TextNode(blocks, TextType.TEXT)
    blocks = text_node_to_html_node(blocks)
    blocks = ParentNode("code", [blocks])
    return  ParentNode("pre", [blocks])
    
# =======================================================================================
def check_heading(text):
    """This function checks that the heading is valid and returns a count of the heading"""
    pattern = ['# ', '## ', '### ', '#### ', '##### ', '###### ']
    for x in pattern:
        if text.startswith(x):
            return len(x.strip())
    raise Exception('invalid pattern')
# ! HEADINGS
def headings_to_html(block):
    blocks = block.split("\n")
    nodes = []
    
    for block in blocks:
        heading = check_heading(block)
        text_nodes = text_to_textnodes(block.lstrip("# "))
        html_nodes = [text_node_to_html_node(node) for node in text_nodes]

        nodes.append(ParentNode(f"h{heading}", html_nodes))
    return nodes 
# =======================================================================================
