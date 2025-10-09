import unittest
from delimiter import split_nodes_delimiter
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


def test_split_nodes_delimiter(self):
    node1 = TextNode("this is **bold** text", TextType.TEXT)
    node2 = TextNode("this is *italic* text", TextType.TEXT)
    node3 = TextNode("this is normal text", TextType.TEXT)
    node4 = TextNode(" to print`print('hello world')`", TextType.TEXT)
    new_list = split_nodes_delimiter(node1, '**', TextType.BOLD)
    new_list2 = split_nodes_delimiter(node2, '*', TextType.ITALIC)
    new_list3 = split_nodes_delimiter(node3, '**', TextType.BOLD)
    new_list4 = split_nodes_delimiter(node4, '`', TextType.CODE)
    expected_list = [
        TextNode("this is ", TextType.TEXT),
        TextNode("bold", TextType.BOLD),
        TextNode(" text", TextType.TEXT)
    ]
    expected_list2 = [
        TextNode("this is ", TextType.TEXT),
        TextNode("italic", TextType.ITALIC),
        TextNode(" text", TextType.TEXT)
    ]
    expected_list3 = [TextNode("this is normal text", TextType.TEXT)]
    expected_list4 = [
        TextNode(" to print", TextType.TEXT),
        TextNode("print('hello world')", TextType.CODE)
    ]
    self.assertEqual(new_list, expected_list)
    self.assertEqual(new_list2, expected_list2)
    self.assertEqual(new_list3, expected_list3)
    self.assertEqual(new_list4, expected_list4)


if __name__ == "__main__":
    unittest.main()
