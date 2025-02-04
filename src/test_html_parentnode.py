import unittest

from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):
    def test_parents_0(self):
        node_2 = LeafNode("p", "Hello mr. beans", None)
        node_3 = ParentNode("a", [node_2], {"href": "https://www.google.com"})

        expected_html = '<a href="https://www.google.com"><p>Hello mr. beans</p></a>'

        self.assertEqual(node_3.to_html(), expected_html)
    
    def test_parents_1(self):
        node_2 = LeafNode("p", "Hello mr. beans", None)
        node_3 = ParentNode("a", [node_2], {"href": "https://www.google.com"})
        node_1 = ParentNode("head", [node_3], None)

        expected_html = '<head><a href="https://www.google.com"><p>Hello mr. beans</p></a></head>'

        self.assertEqual(node_1.to_html(), expected_html)

    def test_parents_2(self):
        node = ParentNode("p",
                            [
                                LeafNode("b", "Bold text"),
                                LeafNode(None, "Normal text"),
                                LeafNode("i", "italic text"),
                                LeafNode(None, "Normal text"),
                            ]
                        )
        expected_html = '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'
        self.assertEqual(node.to_html(), expected_html)

    def test_parents_3(self):
        node = ParentNode("p",
                            [
                                ParentNode("i",[LeafNode("b", "Bold text")]),
                                ParentNode("p",[LeafNode("b", "Bold text"),
                                                LeafNode("a", "linky boy", {"href":"link.com"}),
                                                LeafNode(None, "parino")
                                                ]),
                                LeafNode("i", "italic text"),
                                LeafNode(None, "Normal text"),
                            ]
                        )
        expected_html = '<p><i><b>Bold text</b></i><p><b>Bold text</b><a href="link.com">linky boy</a>parino</p><i>italic text</i>Normal text</p>'
        self.assertEqual(node.to_html(), expected_html)

    def test_parents_4(self):
        node = ParentNode("p",
                    [
                        ParentNode(None,[LeafNode("b", "Bold text")]),
                        ParentNode("p",[LeafNode("b", "Bold text"),
                                        LeafNode("a", "linky boy", {"href":"link.com"}),
                                        LeafNode(None, "parino")
                                        ]),
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text"),
                    ]
                )
        self.assertRaises(ValueError, node.to_html)

    def test_parents_5(self):
        node = ParentNode("p",
                    [
                        ParentNode(None,[LeafNode("b", "Bold text")]),
                        ParentNode("a",[None], props={"href": "nuggets.web"}),
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text"),
                    ]
                )
        self.assertRaises(ValueError, node.to_html)

    def test_parents_6(self):
        node = ParentNode("p",[])
        self.assertEqual('<p></p>', node.to_html())

if __name__ == "__main__":
    unittest.main()
