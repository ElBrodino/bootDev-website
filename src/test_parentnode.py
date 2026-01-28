import unittest

from leafNode import LeafNode
from parentNode import ParentNode


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_parent_no_tag(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(None, [child_node])
        self.assertRaises(ValueError)
        # if self.tag is None:
        #    raise ValueError("Missing tag")

    # def test_parent_no_value(self):
    #    child_node = LeafNode("span", "child")
    #    parent_node = ParentNode("p", value="test", children=[child_node])
    #    self.assertRaises(ValueError)
    #    if self.value is not None:
    #        raise ValueError("Missing Value")
