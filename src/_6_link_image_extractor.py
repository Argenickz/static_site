import re




#! Assignment
#1.  Write a function, 'extract_markdown_images(text) that takes raw markdown text and returns a lisf of tuples. Each tuple should contain the alt_text and the URL of any markdown images for example:

image = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
# print(extract_markdown_images(text))
# [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


# print(extract_markdown_images(image))



# 2. Write a similar function 'extract_markdown_links(text)' that extracts markdown links instead of images. It should return tuples of anchor text and URLs. For example:
link = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
# print(extract_markdown_links(text))
# [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)

