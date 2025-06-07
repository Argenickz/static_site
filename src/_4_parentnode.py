from _2_htmlnode import HTMLNode
from _3_leafnode import LeafNode
# Create a new child class of HTMLNode called ParentNode. Its constructor should differ from HTMLNode in that:
    # . The tag and children arguments are not optional
    # . It doesn't take a value argument
    # . props is optional
    # . (It's the exact opposite of the LeafNode class)
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    # Add a 'to_html' method.
    # . If the object doesn't have a tag, raise a ValueError.
    # . If the children is missing value, raise a ValueError with a different message.
    # . Otherwise, return a string representing the HTML tag of this node and its children. This should be a recursive method (each recursion being called on a nested child node).
    def to_html(self):
        if len(self.tag) < 1 or self.tag == None:
            raise ValueError("A tag is necessary for a parent node")
        if not self.children or self.children == None:
            raise ValueError("Children needs to have value and need to be passed as a list")
        value = f"<{self.tag}{self.props_to_html()}>" + ''.join(child.to_html() for child in self.children) + f"</{self.tag}>"
        return value
    

    def __repr__(self):
        return f"ParentNode(tag: {self.tag}, children: {self.children}, props: {self.props})"


