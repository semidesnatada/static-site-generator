import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_1(self):
        html_node_0 = HTMLNode(None, "Press this to go to google", None, None)
        html_node_1 = HTMLNode("p", "Hello mr. beans", None, None)
        html_node_2 = HTMLNode("a", None, html_node_0, {"href": "https://www.google.com"})
        self.assertEqual(html_node_0.props_to_html(), "")

    def test_props_2(self):
        html_node_1 = HTMLNode("p", "Hello mr. beans", None, None)
        self.assertEqual(html_node_1.props_to_html(), "")

    def test_props_3(self):
        html_node_0 = HTMLNode(None, "Press this to go to google", None, None)
        html_node_2 = HTMLNode("a", None, html_node_0, {"href": "https://www.google.com"})
        self.assertEqual(html_node_2.props_to_html(), ' href="https://www.google.com"')

    def test_error_raised(self):
        html_node_0 = HTMLNode(None, "Press this to go to google", None, None)
        self.assertRaises(NotImplementedError, html_node_0.to_html)

if __name__ == "__main__":
    unittest.main()
