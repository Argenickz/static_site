from _2_htmlnode import HTMLNode

# 1. Create a child class of HTMLNode called LeafNode. Its constructor should differ slightly from the HTMLNode class:
# . It should not allow for any children
# . The value data member should be required (and tag even though the tag's value may be None)
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None,  props)

    # Add a 'to_html() method that renders a leaf node as an HTML string(by returning a string).
    #   . If the leafnode has no value, it should raise a ValueError. All the leafnode must have value
    #   . If there is no tag (e.g. it's None), the value should be returned as raw text.
    #   . Otherwise, it should render an HTML tag. for example:
    # `LeafNode("p", "This is a paragraph of text.").to_html()
        "<p>This is a paragraph of text.</p>"

    # `LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html()
        '<a href="https://www.google.com">Click me!</a>'

    def to_html(self):
        if self.value == None:
            raise ValueError("All leafnodes must have value")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    # Check for props
    
    def __repr__(self):
        return f"LeafNode(tag: {self.tag}, value: {self.value}, props: {self.props})"
    







        