from enum import Enum

# Create an enum called TextType, it should cover all the types of text nodes mentioned in the lesson
class TextType(Enum):
    TEXT = "TEXT"
    BOLD = "BOLD"
    ITALIC = "ITALIC"
    CODE = "CODE"
    LINK = "LINK"
    IMAGE = "IMAGE"

# In textnode.py create a class called TextNode. It should have 3 properties that can be set in the constructor: 
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
    

# Todo working here
def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            pass



# debug 
def main():
    print(text_node_to_html_node(TextNode('this is some text', TextType.TEXT)))
    print(text_node_to_html_node(TextNode('this is bold text', TextType.BOLD)))
    print(text_node_to_html_node(TextNode('this is italic text', TextType.ITALIC)))



    

if __name__ == "__main__":
    main()

