class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        # A string representing the HTML tag name
        # (e.g. "p", "a", "h1", etc.)
        self.tag = tag
        # A string representing the value of the HTML tag
        # (e.g. the text inside a paragraph)
        self.value = value
        # A list of HTMLNode objects representing the children of
        self.children = children
        # A dictionary of key-value pairs representing
        # the attributes of the HTML tag.
        # For example, a link (<a> tag) might have
        # {"href": "https://www.google.com"}
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if self.props is None:
            return None

        string = f"href={self.props}"
        return string

    def __eq__(self, other):  # members : tag, value, children, props
        if (
            self.tag == other.tag
            and self.value == other.value
            and self.children == other.children
            and self.props == other.props
        ):
            return True
        return False

    def __ne__(self, other):
        if (
            self.tag != other.tag
            or self.value != other.value
            or self.children != other.children
            or self.props != other.props
        ):
            return True
        return False

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
