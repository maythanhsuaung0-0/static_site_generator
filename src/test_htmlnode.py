import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode
from main import text_node_to_html_node
from textnode import TextNode, TextType


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node1 = HTMLNode('a', 'hello', None, {
            "href": "https://www.google.com",
            "target": "_blank",
        })
        self.assertEqual(node1.props_to_html(),
                         " href='https://www.google.com' target='_blank'")

    def test_notEq(self):
        node1 = HTMLNode('p', 'hello', '<span>hey</span>', {
            "href": "https://www.google.com",
        })
        node2 = HTMLNode('p', 'hello', '<span>hey</span>', {
            "href": "https://www.google.com",
            "target": "_blank",
        })
        self.assertNotEqual(node1, node2)

    def test_leafNode_to_html(self):
        node1 = LeafNode("p", "hello")
        self.assertEqual(node1.to_html(), "<p>hello</p>")

    def test_leafNode_with_props_to_html(self):
        node1 = LeafNode(
            "a", "click",
            {"class": "paragraph", "href": "https://www.youtube.com"})
        self.assertEqual(
            node1.to_html(),
            "<a class='paragraph' href='https://www.youtube.com'>click</a>")

    def test_to_html_with_children(self):
        child = LeafNode("p", "hello")
        parent = ParentNode("div", [child], {"class": "parent"})
        self.assertEqual(
            parent.to_html(), "<div class='parent'><p>hello</p></div>")

    def test_to_html_with_grandchildren(self):
        grandkid = LeafNode("a", "load more", {
                            "href": "https://www.google.com"})
        child = ParentNode("div", [grandkid])
        parent = ParentNode("div", [child], {"id": "parent1"})
        self.assertEqual(
            parent.to_html(),
            "<div id='parent1'><div><a href='https://www.google.com'>load more</a></div></div>"
        )


def test_text(self):
    node = TextNode("hello", TextType.BOLD, "")
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.to_html(), "<b>hello</b>")
    self.assertEqual(html_node.tag, "b")


if __name__ == "__main__":
    unittest.main()
