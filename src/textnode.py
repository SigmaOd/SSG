from htmlnode import LeafNode
from enum import Enum


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    if text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    raise ValueError(f"Invalid text type: {text_node.text_type}")


    # def text_node_to_html_node(text_node):
    #     match text_node.text_type:
    #         case text_node.text_type.TEXT:
    #             leaf_node = LeafNode(None, text_node.text)
    #             return leaf_node.to_html()
    #         case text_node.text_type.BOLD:
    #             leaf_node = LeafNode("b", text_node.text)
    #             return leaf_node.to_html()
    #             # return LeafNode.to_html("b", text_node.text)
    #         case text_node.text_type.ITALIC:
    #             leaf_node = LeafNode("i", text_node.text)
    #             return leaf_node.to_html()
    #             # return LeafNode.to_html("i", text_node.text)
    #         case text_node.text_type.CODE:
    #             leaf_node = LeafNode("code", text_node.text)
    #             return leaf_node.to_html()
    #             # return LeafNode.to_html("code", text_node.text)
    #         case text_node.text_type.LINK:
    #             url = text_node.url
    #             prop= {
    #                 "href": url,
    #             }
    #             leaf_node = LeafNode("a", text_node.text, props=prop)
    #             return leaf_node.to_html()
    #             # propped_text = f' href="{text_node.url}"'
    #             # return LeafNode.to_html("a",text_node.text, props)
    #         case text_node.text_type.IMAGE:
    #             url = text_node.url
    #             alt_text = text_node.text
    #             prop= {
    #                 "src": url,
    #                 "alt": alt_text,
    #             }
    #             # string_propped = f'<img src="{text_node.url}" alt="{text_node.text}">'
    #             # alt_propped = f' alt="{text_node.text}'
    #             leaf_node = LeafNode("img", text_node.text, props=prop)
    #             return leaf_node.to_html()
    #         case _:
    #             raise Exception("Text_Type not valid")
            

        

#
##
###
####
#####
### pre solution_check: unneccessary strings in the enum, unneccessary if condition in __eq__; went back and forth on .value in __repr_
#
# class TextType(Enum):
#     NORMAL_TEXT = "normal text"
#     BOLD_TEXT = "bold text"
#     ITALIC_TEXT = "italic text"
#     CODE = "code"
#     LINK = "link"
#     IMAGE = "image"


# class TextNode():
#     def __init__(self, text, text_type, url=None):
#         self.text = text
#         self.text_type = text_type
#         self.url = url


#     def __eg__(self, other):
#         if (self.text and self.text_type and self.url) == (other.text and other.text_type and other.url):
#             return True
    
#     def __repr__(self):
#         return f"{TextNode}({self.text}, {self.text_type}, {self.url})"



