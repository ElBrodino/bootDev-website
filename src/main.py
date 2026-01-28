from htmlnode import HTMLNode
from textnode import TextNode, TextType


def main():
    print(TextNode("dude", TextType.LINK, "https://www.boot.dev"))
    print(HTMLNode())


main()
