from typing_extensions import NoDefault

from htmlnode import HTMLNode
from leafNode import LeafNode
from parentNode import ParentNode
from textnode import TextNode, TextType


def main():
    print(TextNode("dude", TextType.LINK, "https://www.boot.dev"))
    print(f"textNode type : {type(TextNode('dude2', TextType.LINK, 'www.dude.com'))}")
    print(
        HTMLNode(
            "p",
            "This is the text inside a paragraph",
            [HTMLNode("p"), HTMLNode("p")],
            {"href": "https://www.google.com"},
        )
    )
    test = LeafNode("p", "This is a leaf node")
    print(test)
    print(test.to_html())
    print(test.props_to_html())
    test2 = LeafNode(
        "a", "Click me!", {"href": "https://www.google.com", "target": "_blank"}
    )
    print(test2)
    print(test2.to_html())
    print(f"props_to_html : {test2.props_to_html()}")
    test3 = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )
    print(test3.to_html())


main()
