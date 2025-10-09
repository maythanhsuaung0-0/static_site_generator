import unittest
from textnode import TextType, TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node, node2)

    def test_notEq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a bold node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_almostEq(self):
        node = TextNode("This is a text node 1", TextType.TEXT)
        node2 = TextNode("This is a text node 2", TextType.TEXT)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
