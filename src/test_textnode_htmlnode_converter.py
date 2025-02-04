import unittest

from htmlnode import LeafNode
from textnode import TextNode, TextType, text_node_to_html_node

class TestHTMLNode(unittest.TestCase):
    def test_normal(self):
        text_node = TextNode("Baked Beans", TextType.NORMAL_TEXT)
        expected_html_node = LeafNode(None, "Baked Beans", None)
        self.assertEqual(text_node_to_html_node(text_node), expected_html_node)

    def test_italic(self):
        text_node = TextNode("Baked Beans", TextType.ITALIC_TEXT)
        expected_html_node = LeafNode("i", "Baked Beans", None)
        self.assertEqual(text_node_to_html_node(text_node), expected_html_node)

    def test_bold(self):
        text_node = TextNode("Baked Beans", TextType.BOLD_TEXT)
        expected_html_node = LeafNode("b", "Baked Beans", None)
        self.assertEqual(text_node_to_html_node(text_node), expected_html_node)

    def test_code(self):
        text_node = TextNode("Baked Beans", TextType.CODE_TEXT)
        expected_html_node = LeafNode("code", "Baked Beans", None)
        self.assertEqual(text_node_to_html_node(text_node), expected_html_node)

    def test_link(self):
        text_node = TextNode("This is not a text node", TextType.LINKS, "great-web-com")       
        expected_html_node = LeafNode("a", "This is not a text node", {'href': "great-web-com"})
        self.assertEqual(text_node_to_html_node(text_node), expected_html_node)

    def test_image(self):
        text_node = TextNode("This is not a text node", TextType.IMAGES, "great-web-com")
        expected_html_node = LeafNode("img", "", {'alt':"This is not a text node" , 'src': "great-web-com"})
        self.assertEqual(text_node_to_html_node(text_node), expected_html_node)

    def test_invalid(self):
        text_node = TextNode("This is not a valid text type", None, "great-web-com")
        self.assertRaises(Exception, text_node_to_html_node, text_node)

if __name__ == "__main__":
    unittest.main()
