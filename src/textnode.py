from enum import Enum
from htmlnode import LeafNode, ParentNode

class TextType(Enum):
    NORMAL_TEXT = "normal text"
    BOLD_TEXT = "bold text"
    ITALIC_TEXT = "italic text"
    CODE_TEXT = "code text"
    CODE_BLOCK = "code block"
    LINKS = "links"
    IMAGES = "images"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node):

    match text_node.text_type:
        case TextType.NORMAL_TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD_TEXT:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC_TEXT:
            return LeafNode("i", text_node.text)
        case TextType.CODE_TEXT:
            return LeafNode("code", text_node.text, {"class": "inline hljs language-python"})
        case TextType.CODE_BLOCK:
            return ParentNode("pre", [LeafNode("code", text_node.text, {"class": "block"})])
        case TextType.LINKS:
            return LeafNode("a", text_node.text, {"href":text_node.url})
        case TextType.IMAGES:
            return LeafNode("img", "", {"src":text_node.url,
                                        "alt":text_node.text})
        case _:
            raise Exception("Input is not a valid type for conversion")