import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node2", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")

    # def test_node_to_html_node_text(self):
    #     node = TextNode("This is a text node", TextType.TEXT)
    #     self.assertEqual(
    #         "This is a text node", node.text_node_to_html_node()
    #     )
    # def test_node_to_html_node_bold(self):
    #     node = TextNode("This is a bold text node", TextType.BOLD)
    #     self.assertEqual(
    #         "<b>This is a bold text node</b>", node.text_node_to_html_node()
    #     )
    # def test_node_to_html_node_italic(self):
    #     node = TextNode("This is a italic text node", TextType.ITALIC)
    #     self.assertEqual(
    #         "<i>This is a italic text node</i>", node.text_node_to_html_node()
    #     )
    # def test_node_to_html_node_code(self):
    #     node = TextNode("This is a code text node", TextType.CODE)
    #     self.assertEqual(
    #         "<code>This is a code text node</code>", node.text_node_to_html_node()
    #     )   
    # def test_node_to_html_node_link(self):
    #     # url = "https://www.google.com"
    #     node = TextNode("This is a link text node", TextType.LINK, "https://www.google.com")
    #     self.assertEqual(
    #         '<a href="https://www.google.com">This is a link text node</a>', node.text_node_to_html_node()
    #     )
    # def test_node_to_html_node_img(self):
    #     url = "url/of/image.jpg"
    #     node = TextNode("Description of image", TextType.IMAGE, url)
    #     self.assertEqual(
    #         '<img src="url/of/image.jpg" alt="Description of image">', node.text_node_to_html_node()
        # )
    
    # def test_eq(self):
    #     node = TextNode("This is a text node", TextType.BOLD)
    #     node2 = TextNode("This is a text node", TextType.BOLD)
    #     self.assertEqual(node, node2)


    # def test_repr_eq(self):
    #     node = TextNode("This is not a text node", TextType.ITALIC)
    #     node2 = TextNode("This is not a text node", TextType.ITALIC)
    #     self.assertEqual(node, node2)

    # def test_eq_url_None(self):
    #     node = TextNode("This is a text node", TextType.BOLD, url=None)
    #     node2 = TextNode("This is a text node", TextType.BOLD, url=None)
    #     self.assertEqual(node, node2)

    # def test_false_diff_ttype(self):
    #     node = TextNode("This is a text node", TextType.ITALIC)
    #     node2 = TextNode("This is a text node", TextType.BOLD)
    #     self.assertNotEqual(node, node2)

    # def test_text_false(self):
    #     node = TextNode("This is not text node", TextType.ITALIC)
    #     node2 = TextNode("This is not a text node", TextType.ITALIC)
    #     self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()