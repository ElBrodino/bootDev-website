from htmlnode import HTMLNode
from textnode import TextNode, TextType


def main():
    print(TextNode("dude", TextType.LINK, "https://www.boot.dev"))
    print(
        HTMLNode(
            "p",
            "This is the text inside a paragraph",
            [HTMLNode("p"), HTMLNode("p")],
            {"href": "https://www.google.com"},
        )
    )


main()
