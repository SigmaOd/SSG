from enum import Enum


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



