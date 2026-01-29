from leafNode import LeafNode
from textnode import TextType


def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, text_node.prop)
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode(
            "img",
            value=None,
            props={"src": text_node.props["src"], "alt": text_node.props["alt"]},
        )
    else:
        raise Exception("Type is not accepted")
