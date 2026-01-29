import unittest

from text_node_to_html_node import text_node_to_html_node
from textnode import TextNode, TextType


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a plain text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a plain text node")

    def test_bold(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.value, node.text)
        self.assertEqual(html_node.tag, "b")

    def test_italic(self):
        node = TextNode("This is a italic text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.value, node.text)
        self.assertEqual(html_node.tag, "i")

    def test_code(self):
        node = TextNode("This is a text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.value, node.text)
        self.assertEqual(html_node.tag, "code")
