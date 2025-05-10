# Define a class called HTMLNode
# The HTMLNode class should have 4 data members set in the constructor
# tag (A string representing the HTML tag name(e.g. 'p', 'a' 'h1', etc.))
# value (A string representing the value of the HTML tag (e.g. the text in a paragraph))
# children (A list of HTMLNode objects representing the children of this node)
# props (A dictionary of key value pairs representing the attributes of the HTML tag. for example a link (<a>) might have {"href": "https://www.google.com"})
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    # Add a self.props_to_html() function. It should return a string representing the HTML attributes of the node. For example:
    #` {"href": "https://www.google.com", "target": "_blank"}
    #` Should become this:  href="https://www.google.com" target="_blank"
    def props_to_html(self):
        result = ''.join(f' {prop}="{self.props[prop]}"' for prop in self.props)
        return result

    # Add a __repr__ method. Give yourself a way to print an HTMLNode object an see its tag, value, children, and props. This will be useful for debugging. 
    def __repr__(self):
        return f"HTMLNode(tag: {self.tag}, value:{self.value}, children:{self.children}, props:{self.props_to_html()})"

    # Create some tests for the HTMLNode, make them in a new file if you'd like.


test = {"href": "https://www.google.com", "target": "_blank"}

node = HTMLNode("p", "some text", None, test)
print(node)


# Todo create a file tomorrow and run unittests
