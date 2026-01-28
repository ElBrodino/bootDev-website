import unittest

from htmlnode import HTMLNode
from leafNode import LeafNode
from textnode import TextNode, TextType


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node, node2)
        self.assertFalse(node != node2)

    def test_ne(self):
        node = HTMLNode()
        node2 = HTMLNode("Dude")
        self.assertNotEqual(node, node2)
        self.assertFalse(node == node2)

    # members : tag, value, children, props
    def test_ne_tag(self):
        node = HTMLNode(tag="test")
        node2 = HTMLNode(tag="test2")
        self.assertNotEqual(node, node2)
        self.assertFalse(node == node2)

    def test_ne_value(self):
        node = HTMLNode(value="test")
        node2 = HTMLNode(value="test2")
        self.assertNotEqual(node, node2)
        self.assertFalse(node == node2)

    def test_ne_children(self):
        node = HTMLNode(
            children=[TextNode("dude", TextType.BOLD), TextNode("dude2", TextType.BOLD)]
        )
        node2 = HTMLNode(children=[TextNode("dude", TextType.PLAIN)])
        self.assertNotEqual(node, node2)
        self.assertFalse(node == node2)

    def test_ne_props(self):
        node = HTMLNode(props={"href": "https://www.google.com"})
        node2 = HTMLNode(props={"href": "https://www.outlook.com"})
        self.assertNotEqual(node, node2)
        self.assertFalse(node == node2)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(), '<a href="https://www.google.com">Click me!</a>'
        )

    def test_leaf_to_html_no_value(self):
        node = LeafNode("a", value=None)
        self.assertRaises(ValueError)

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(
            tag=None,
            value="Click me!",
        )
        self.assertEqual(node.to_html(), "Click me!")


if __name__ == "__main__":
    unittest.main()
