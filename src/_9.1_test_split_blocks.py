import unittest
from _9_split_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items"
            ]
        )

    def test_empty_new_lines(self):
        md = """

There is a new line above this that needs to be deleted


This paragraph is a place holder
this is the same paragraph in a new line


- This list has two items:
- first item
- second item (there is a new line at the end here that needs deleting)


"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "There is a new line above this that needs to be deleted",
                "This paragraph is a place holder\nthis is the same paragraph in a new line",
                "- This list has two items:\n- first item\n- second item (there is a new line at the end here that needs deleting)"
            ]
        )

if __name__ == "__main__":
    unittest.main()