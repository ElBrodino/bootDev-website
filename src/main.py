from textnode import TextNode, TextType


def main():
    # link = TextType
    test = TextNode("dude", TextType.LINK, "https://www.boot.dev")
    print(test)


main()
