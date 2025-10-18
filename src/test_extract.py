import unittest
from extract import extract_markdown_images


class Test_Extractor(unittest.TestCase):
    def test_extract_markdown_images(self):
        matcher = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        print(matcher)
        self.assertListEqual(
            [("image", "https://i.imgur.com/zjjcJKZ.png")], matcher)


if __name__ == "__main__":
    unittest.main()
