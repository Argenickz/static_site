import unittest
from link_image_extractor import extract_markdown_images, extract_markdown_links


class LinkImageExtractor(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://www.i.imagur.com/123abc.png)"
        )
        self.assertEqual([("image", "https://www.i.imagur.com/123abc.png")], matches)

    def test_extract_markdown_link(self):
        link = extract_markdown_links("this is the link you wanted [to youtube](https://www.youtube.com)")
        self.assertEqual([("to youtube", "https://www.youtube.com")], link)

    def test_multiple_links(self):
        links = "these are the links [link one](https://www.link1.com) and this [link two](https://www.link2.com)"
        link_list = extract_markdown_links(links)
        self.assertEqual(
            [("link one", "https://www.link1.com"), ("link two", "https://www.link2.com")],
            link_list
        )

    


if __name__ == "__main__":
    unittest.main()