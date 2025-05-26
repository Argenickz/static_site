from pprint import pprint
"""
! Split Blocks

Our static site generator only cares about two things:
. Inline markdown
. Block markdown

Inline markdown is what we just took care of. It's the stuff that's inside of a block. For example, the **bolded** text in this sentence is inline markdown.

Block-level markdown is just the separation of different sections of an entire document. In well-written markdown (which we'll just assume is the only think going in our generator)blocks are separated by a single blank line. 
Here are 3 distinct blocks:

# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside it.

- This is the first list item in a list block
- this is a list item
- This is another list item

The heading, the paragraph, and the unordered list are all separate blocks. The blank line between them is what separates them.


!Assignment
1. Create a new function called 'markdown_to_blocks(markdown)'. It takes a raw markdown string (representing a full document) as input and returns a list of 'block' strings The example above would be split into these three strings:

# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside it.

- This is the first list item in a list block
- this is a list item
- This is another list item


. The .split() method can be used to split a string into blocks based on a delimiter (\n\n) is a double new line.

. You should .strip() any leading or trailing whitespaces from each block.

. Remove any empty new lines due to excessive new lines.

(Notice the indentation of the multiline string! New lines shouldn't be indented because the tab will be included in the string and your tests will fail.)

    def test_markdown_to_blocks(self):
        md = """
# This is **bolded** paragraph

# This is another paragraph with _italic_ text and `code` here
# This is the same paragraph on a new line

# - This is a list
# - with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

"""
def markdown_to_blocks(markdown):
    # split 'delimiter'
    double_line = "\n\n"

    # create a list from the text of items, split at the double line
    split_list = markdown.split(double_line)

    # Create an empty list to catch all the new items
    corrected_list = []

    # Run a loop for all the items
    for block in split_list:

        # Get rid of all the unnecessary empty new lines at the beginning or end of the item text
        stripped = block.rstrip("\n").lstrip("\n")

        # If the item is not empty add it to the final list and return the final list.
        if len(stripped) > 1:
            
            corrected_list.append(stripped) 
    return corrected_list

def main():
    """This is an example test for reference"""
    markdown = """
This is a **bolded** paragraph

This is another paragraph with _italic_ and `code` text here

- This is the first list item in a list block
- this is a list item
- This is another list item
"""
    pprint(markdown_to_blocks(markdown))

if __name__ == "__main__":
    main()
