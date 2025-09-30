from enum import Enum


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "anchor"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url=None) -> None:
        self.text = text
        self.text_type = TextType(text_type)
        self.url = url

    def __eq__(self, other: object, /) -> bool:
        if isinstance(other, TextNode):
            identical = (self.text == other.text and
                         self.text_type == other.text_type and
                         self.url == other.url)
            return identical
        return False

    def __repr__(self) -> str:
        return f"TextNode({self.text},{self.text_type.value},{self.url})"
