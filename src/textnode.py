from enum import Enum
from leafnode import LeafNode
# Create an enum called TextType, it should cover all the types of text nodes mentioned in the lesson
class TextType(Enum):
    TEXT = "TEXT"
    BOLD = "BOLD"
    ITALIC = "ITALIC"
    CODE = "CODE"
    LINK = "LINK"
    IMAGE = "IMAGE"

# In text node.py create a class called TextNode. It should have 3 properties that can be set in the constructor: 
# self.text (the text content of the node)
# self.text_type (the type of text this node contains, which is a member of the TextType enum)
# self.url (the URL of the link or image, if the text is a link. Default to None if nothing is passed in.)
class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url


# Create an __eq__ method that returns True if all of the properties of two TextNode objects are equal. Our future unit tests will rely on this method to compare objects.
    def __eq__(self, other):
        return(
            self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url
        )

# Create a __repr__ method that returns a string representation of the TextNode object. It should look like this:
# TextNode(TEXT, TEXT_TYPE, URL)
# Where those are the values of text, text_type and url respectively
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    

# Write a function 'text_node_to_html()
# It should handle each type of TexType enum, if it gets a text node that is none of those types it should raise an exception. Otherwise, it should return a new LeafNode object
# TextType.Text should return a LeafNode with no tag, just a raw text value
# TextType.BOLD should return  a LeafNode with a 'b' tag and the text
# TextType.ITALIC should return a LeafNode with an 'i' tag and the text
# TextType.CODE 'i' tag, text.
# TextType.LINK: "a" tag, anchor text, and "href" prop
# TextType.IMAGE: "img" tag, empty string value, "src" and "alt" props ("src" is the image URL, "alt" is the alt text)
def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href":text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", '', {"src":text_node.url, "alt":text_node.text})
        case _:
            raise Exception("Text type needs to match")
        
        # Todo write unit tests tomorrow.



# debug 
def main():
    print(text_node_to_html_node(TextNode('this is some text', TextType.TEXT)).to_html())
    print(text_node_to_html_node(TextNode('this is bold text', TextType.BOLD)).to_html())
    print(text_node_to_html_node(TextNode('this is italic text', TextType.ITALIC)).to_html())
    print(text_node_to_html_node(TextNode('this is code text', TextType.CODE)).to_html())
    print(text_node_to_html_node(TextNode("this is some anchor text", TextType.LINK, "https://www.google.com")).to_html())
    print(text_node_to_html_node(TextNode("this is the image description", TextType.IMAGE, "https://www.imgur.com")).to_html())
    
    




    

if __name__ == "__main__":
    main()

