import unittest
from htmlnode import HTMLNode
from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    # def test_to_html1(self):
    #     # value none: ValueError("value cannot be None") 
    #     # tag = "p"
    #     # value = None
    #     node = LeafNode("p", None)
    #     self.assertEqual("ValueError: value cannot be None", node.to_html())
    
    def test_to_html2(self):
        #  if self.tag == None:
        #     return f"{self.value}"
        node = LeafNode(None, "None is None when None is None")
        self.assertEqual("None is None when None is None", node.to_html())



    def test_to_html3(self):
# f"<{self.tag}>{self.value}</{self.tag}>"
        node = LeafNode("h1", "This is a Heading 1")
        self.assertEqual("<h1>This is a Heading 1</h1>", node.to_html())


# class TestHtmlNode(unittest.TestCase):
#     def test_props_to_html_none(self):
#         node = HTMLNode(tag=None, value=None, children=None, props=None)
#         self.assertEqual(
#             node.props_to_html(),
#             "",
#         )

#     def test_to_html_props(self):
#         node = HTMLNode(
#             "div",
#             "Hello, world!",
#             None,
#             {"class": "greeting", "href": "https://boot.dev"},
#         )
#         self.assertEqual(
#             node.props_to_html(),
#             ' class="greeting" href="https://boot.dev"',
#         )
#     def test_values(self):
#         node = HTMLNode(
#             "div",
#             "I wish I could read",
#         )
#         self.assertEqual(
#             node.tag,
#             "div",
#         )
#         self.assertEqual(
#             node.value,
#             "I wish I could read",
#         )
#         self.assertEqual(
#             node.children,
#             None,
#         )
#         self.assertEqual(
#             node.props,
#             None,
#         )