from enum import Enum


class TextType(Enum):
    PLAIN = "plain"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGES = "images"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = TextType(text_type)
        self.url = url

    def __eq__(self, other):
        return True

    def __repr__(self):  # TextNode(TEXT, TEXT_TYPE, URL)
        text_string = f"TextNode({self.text}, {self.text_type.value}, {self.url})"
        return text_string
