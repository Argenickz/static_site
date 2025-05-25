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

# Todo this is just a test run to make sure I understand the logic, once I get it down, we're going to be writing additional helper functions to make the code more readable and concise.
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
    node_list = []

    # Loop over each block
    for block in markdown_blocks:
        
        # Determine the type of block (block_type)
        block_type = block_to_block_type(block)
        

        # Check if the code block is a paragraph
        if block_type == BlockType.PARAGRAPH:
            # adds the children returned by this function to the list
            node_list.append(paragraph_to_html(block))

        if block_type == BlockType.UNORDERED_LIST:
            node_list.append(list_to_html(block, "ul"))
        
        if block_type == BlockType.ORDERED_LIST:
            node_list.append(list_to_html(block, "ol"))

        if block_type == BlockType.QUOTE:
            node_list.append(quote_to_html(block))

        if block_type == BlockType.CODE:
            node_list.append(code_to_html(block))

        if block_type == BlockType.HEADING:
            node_list.extend(headings_to_html(block))
    
    # Returns the children in the list under a single 'div' tag
    return ParentNode("div", node_list)
            
# ====================================================================================
            
def paragraph_to_html(block):
    children = text_to_textnodes(block.replace("\n", " "))
    child_list = [text_node_to_html_node(son) for son in children]
    return ParentNode("p", child_list)
# =======================================================================================
def list_to_html(block, order):
    blocks = block.split("\n")
    blocks = list(map(lambda text: text.lstrip("- "), blocks))
    children = list(map(lambda item: text_to_textnodes(item), blocks))
    child_list = [text_node_to_html_node(item) for [item] in children]
    grand_children = list(map(lambda child: ParentNode("li", [child]), child_list))
    return ParentNode(order, grand_children)
# =======================================================================================
def quote_to_html(block):
    blocks = block.split("\n")
    blocks = list(map(lambda line: line.replace(">", " "), blocks))
    children = list(map(lambda item: text_to_textnodes(item), blocks))
    child_list = [text_node_to_html_node(item) for [item] in children]
    return ParentNode("blockquote", child_list)
# =======================================================================================
# Todo Need to fix this function, it is not necessary to wrap every block in <code> just the whole thing in this pattern: <div><pre><code>Items go here\nWhatever</code></pre></div>
def code_to_html(block):
    # Using replace() with a count argument, like 1, will only replace the first instance of a character
    blocks = block.lstrip("```").rstrip("```").replace("\n", "", 1)
    blocks = TextNode(blocks, TextType.TEXT)
    blocks = text_node_to_html_node(blocks)
    blocks = ParentNode("code", [blocks])
    return  ParentNode("pre", [blocks])
    
# =======================================================================================
# Todo Forgot the headings!! This is wrong run to see the bug
def headings_to_html(block):
    # Use string.count("value") to get the number of '#' characters in the string
    blocks = block.split("\n")
    nodes = []
    count = [block.count("#") for block in blocks]
    children = list(map(lambda item: text_to_textnodes(item.strip("# ")), blocks))
    child_list = [text_node_to_html_node(item) for [item] in children]
    for index in range(len(count)):
        
        nodes.append(ParentNode(f"h{str(index + 1)}", [child_list[index]]))
    return nodes
        
    
    
    
    
    
    
# =======================================================================================
# =======================================================================================
heading = """
# This is heading one
## Number two here
### This is heading three
##### Five is where it's at!
###### Number six is the smallest of the headings
"""

print(markdown_to_html_node(heading).to_html())

all_together = """
- coffee
- milk
- tea
- water

>This is a quote of text, I'm
>not sure what if I'm supposed to add this
>somewhere

This is a **bolded** paragraph
text with a p
tag here

This is another paragraph with _italic_ text and `code` here

1. spaghetti
2. tomato sauce
3. salami
4. onions

```These here are _lines_
of code because they start and
end with the **same** pattern
you just have to pay attention```

"""
# def main():
#     print(markdown_to_html_node(all_together).to_html())

this = """
```
some lines
of python
```
"""
# print(markdown_to_html_node(this).to_html())

# if __name__ == "__main__":
#     main()






