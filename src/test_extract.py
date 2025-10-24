import unittest
from delimiter import split_nodes_image, split_nodes_links
from extract import extract_markdown_images
from md_to_blocks import markdown_to_blocks
from textnode import TextNode, TextType


class Test_Extractor(unittest.TestCase):
    def test_extract_markdown_images(self):
        matcher = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        print(matcher)
        self.assertListEqual(
            [("image", "https://i.imgur.com/zjjcJKZ.png")], matcher)


class Test_splitor(unittest.TestCase):
    def test_split_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        match = split_nodes_image([node])
        self.assertEqual(match, [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE,
                     "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
            )
        ])

    def test_split_link(self):
        node = TextNode(
            "This is text with a [link](https://www.example.com) and another [second link](https://www.test.com)",
            TextType.TEXT,
        )
        match = split_nodes_links([node])
        self.assertEqual(match, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("link", TextType.LINK,
                     "https://www.example.com"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "second link", TextType.LINK, "https://www.test.com"
            )
        ])

    def test_markdown_to_blks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks,
                         ["This is **bolded** paragraph",
                          "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                          "- This is a list\n- with items"])


if __name__ == "__main__":
    unittest.main()
