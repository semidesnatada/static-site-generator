import unittest

from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_props_1(self):
        html_node_0 = LeafNode(None, "Press this to go to google",  None)
        html_node_1 = LeafNode("p", "Hello mr. beans", None)
        html_node_2 = LeafNode("a", None, {"href": "https://www.google.com"})
        self.assertEqual(html_node_0.props_to_html(), "")

    def test_leaf_props_2(self):
        html_node_1 = LeafNode("p", "Hello mr. beans", None)
        self.assertEqual(html_node_1.props_to_html(), "")

    def test_leaf_props_3(self):
        html_node_0 = LeafNode(None, "Press this to go to google", None)
        html_node_2 = LeafNode("a", None, {"href": "https://www.google.com"})
        self.assertEqual(html_node_2.props_to_html(), ' href="https://www.google.com"')

    def test_correct_html_translation_1(self):
        html_node_0 = LeafNode(None, "Press this to go to google", None)
        self.assertEqual("Press this to go to google", html_node_0.to_html())

    def test_correct_html_translation_2(self):
        html_node_1 = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual('<p>This is a paragraph of text.</p>', html_node_1.to_html())

    def test_correct_html_translation_1(self):
        html_node_2 = LeafNode("a", "Click me!", props={"href": "https://www.google.com"})
        self.assertEqual('<a href="https://www.google.com">Click me!</a>', html_node_2.to_html())

if __name__ == "__main__":
    unittest.main()
