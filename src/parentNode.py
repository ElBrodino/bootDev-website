from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children, props)
        self.tag = tag
        self.children = children
        self.props = props

    def to_html(self):
        if self.tag is None:
            raise ValueError("Missing tag")
        if self.value is None:
            raise ValueError("Missing Value")

        answer = f"<{self.tag}>"
        for x in self.children:
            answer += x.to_html()
        answer += f"</{self.tag}>"
        return answer
