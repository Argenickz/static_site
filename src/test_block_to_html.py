import unittest
from _11_block_to_html import markdown_to_html_node

class TestBlockToHtml(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>"
    )
#====================================================================================================================== 
    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html, 
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>"
        )
#====================================================================================================================== 
    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ and `code` here
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> and <code>code</code> here</p></div>"
        )
#======================================================================================================================
    def test_ordered_list(self):
        md = """
1. This is an ordered list
2. With _inline_ text
3. And more **inline** text
4. It also has `python` language
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>This is an ordered list</li><li>With <i>inline</i> text</li><li>And more <b>inline</b> text</li><li>It also has <code>python</code> language</li></ol></div>"
        )
#======================================================================================================================
#======================================================================================================================
#======================================================================================================================
#======================================================================================================================
#======================================================================================================================
#======================================================================================================================

if __name__ == "__main__":
    unittest.main()



