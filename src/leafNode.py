from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props)
        self.tag = tag
        self.text = value
        self.props = props

    def to_html(self):
        if self.text is None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag is None:
            return self.text

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"  # {self.tag}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
