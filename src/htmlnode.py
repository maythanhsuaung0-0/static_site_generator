class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, prop=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.prop = prop

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):

        # {
        #     "href": "https://www.google.com",
        #     "target": "_blank",
        # }
        result = ""
        if self.prop is not None:
            for [key, val] in self.prop.items():
                result += f" {key}='{val}'"
        return result

    def __repr__(self):
        return f"tag is {self.tag}, value is {self.value}, children is {
            self.children} and props {self.prop}"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        result = ""
        if self.value is None:
            raise ValueError("Tag cannot be empty")
        if self.tag is None:
            return self.value
        if self.prop:
            result = self.props_to_html()
        return f"<{self.tag}{result if result else ""}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag cannot be empty")
        if self.children is None:
            raise ValueError("Children cannot be empty")
        html_children = ""
        for child in self.children:
            html_children += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{html_children}</{self.tag}>"

    def __repr__(self):
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


