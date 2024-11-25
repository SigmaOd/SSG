class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Invalid HTML: no value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid HTML: no tag")
        if self.children is None:
            raise ValueError("Invalid HTML: no children")
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
# class HTMLNode():
#     def __init__(self, tag=None, value=None, children=None, props=None):
#         self.tag = tag
#         self.value = value
#         self.children = children
#         self.props = props

#     def to_html(self):
#         raise NotImplementedError("to_html method not implemented")
    
#     def props_to_html(self):
#         if self.props is None:
#             return ""
#         props_html = ""
#         for prop in self.props:
#             props_html += f' {prop}="{self.props[prop]}"'
#         return props_html
#         # string = ""
#         # for key, value in self.props:
#         #     string = f"{string} '{key}'='{value}' "

#         return string
    
#     def __repr__(self):
#         return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
#         # print(f"tag: {self.tag}, value: {self.value}, children: {self.children}, props: '{self.props}'")
    

# class LeafNode(HTMLNode):
#     def __init__(self, tag, value, props=None):
#         super().__init__(tag, value, props)

#     def to_html(self):
#         if self.value == None:
#             raise ValueError("value cannot be None")
#         if self.tag == None:
#             return f"{self.value}"
#         return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


# # class ParentNode(HTMLNode):
# #     def __init__(self, tag, children, props=None):
# #         super().__init__(tag, children, props)
    
# #     def to_html(self):
# class ParentNode(HTMLNode):
#     def __init__(self, tag, children, props=None):
#         super().__init__(tag, None, children, props)

#     def to_html(self):
#         if self.tag is None:
#             raise ValueError("Invalid HTML: no tag")
#         if self.children is None:
#             raise ValueError("Invalid HTML: no children")
#         children_html = ""
#         for child in self.children:
#             children_html += child.to_html()
#         return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

#     def __repr__(self):
#         return f"ParentNode({self.tag}, children: {self.children}, {self.props})"


#         # if self.tag == None:
#         #     raise ValueError("None tag is not a valid tag")
#         # if self.children == []:
#         #     raise ValueError("No Children found")
#         # # parent_syntax = f"<{self.tag}></{self.tag}>"
#         # for child in self.children:
#         #     string = f"<{child[0]}>{child[1]}</{child[0]}>"
#         #     result = string + self.to_html(child)
        
#         # total_string = f"<{self.tag}>{result}</{self.tag}>"
#         # return total_string

#             # f"<{self.tag}>{self.value}</{self.tag}>"

    