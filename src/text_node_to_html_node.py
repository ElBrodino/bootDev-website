from leafNode import LeafNode
from textnode import TextType


# textnode is a TextNode class with parameters:
# text(string), type(TextType), url(string)
def text_node_to_html_node(text_node):
    # TEXT: This should return a LeafNode with no tag, just a raw text value
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    # BOLD: This should return a LeafNode with a "b" tag and the text
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    # ITALIC: i" tag, text
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    # CODE: "code" tag, text
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    # LINK: "a" tag, anchor text, and "href" prop
    elif text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    # IMAGE: "img" tag, empty string value,
    # "src" and "alt" props
    # ("src" is the image URL,
    # "alt" is the alt text)
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode(
            "img",
            "",
            {"src": text_node.url, "alt": text_node.text},
        )
    else:
        raise Exception("Type is not accepted")
