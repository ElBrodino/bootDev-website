import unittest

from htmlnode import HTMLNode
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


if __name__ == "__main__":
    unittest.main()
