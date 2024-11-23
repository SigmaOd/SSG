from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("value cannot be None")
        if self.tag == None:
            return f"{self.value}"
        return f"<{self.tag}>{self.value}</{self.tag}>"