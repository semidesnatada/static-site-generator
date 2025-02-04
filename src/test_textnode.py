import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq_1(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_eq_2(self):
        node = TextNode("This is a text node", TextType.ITALIC_TEXT, None)
        node2 = TextNode("This is a text node", TextType.ITALIC_TEXT, None)
        self.assertEqual(node, node2)

    def test_eq_3(self):
        node = TextNode("This is a text node", TextType.CODE_TEXT, "google")
        node2 = TextNode("This is a text node", TextType.CODE_TEXT, "google")
        self.assertEqual(node, node2)

    def test_eq_4(self):
        node = TextNode("This is a text node", TextType.NORMAL_TEXT, "")
        node2 = TextNode("This is a text node", TextType.NORMAL_TEXT, "")
        self.assertEqual(node, node2)



    def test_different_links(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT, "google.com")
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT, "bbc.co.uk/news")
        self.assertNotEqual(node, node2)
    
    def test_one_missing_link(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT, "google.com")
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertNotEqual(node, node2)
    
    def test_different_texttypes(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT, "google.com")
        node2 = TextNode("This is a text node", TextType.ITALIC_TEXT, "google.com")
        self.assertNotEqual(node, node2)
    
    def test_diff_text_and_texttypes(self):
        node = TextNode("This is a text node", TextType.CODE_TEXT, "google.com")
        node2 = TextNode("ya grandad", TextType.ITALIC_TEXT, "google.com")
        self.assertNotEqual(node, node2)
    
    def test_all_diff(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT, "google.com")
        node2 = TextNode("This is not a text node", TextType.LINKS, "great-web-com")
        self.assertNotEqual(node, node2)




if __name__ == "__main__":
    unittest.main()
