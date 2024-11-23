import unittest
from htmlnode import HTMLNode


class TestHtmlNode(unittest.TestCase):
    def test_props_to_html_none(self):
        node = HTMLNode(tag=None, value=None, children=None, props=None)
        self.assertEqual(
            node.props_to_html(),
            "",
        )

    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )
    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    # def test_props_to_html_link(self):
    #     children = []
    #     props = {"href": "https://www.google.com", 
    #              "target": "_blank",
    #              }
    #     node = HtmlNode("a", "this is a text", children, props)
    #     self.assertEqual("href="https://www.google.com" target="_blank"", repr(node))

    # def test_to_html(self):
    #     node = HTMLNode(tag=None, value=None, children=None, props=None)
    #     self.assertEqual("to_html method not implemented", node.to_html())

    # def test_repr_htmlnode(self):
    #     children = ["child1", "child2"]
    #     props = {"href": "https://www.google.com", 
    #              "target": "_blank",
    #              }
    #     node = HtmlNode("a", "this is a text", children, props)
    #     self.assertEqual("tag: a, value: this is a text, children: ["child1", "child2"], props: '{"href": "https://www.google.com", "target": "_blank",}'", repr(node))

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )


if __name__ == "__main__":
    unittest.main()