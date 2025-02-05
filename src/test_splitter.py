from split_nodes import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_textnodes
from textnode import TextNode, TextType

import unittest

class TestSplitter(unittest.TestCase):
    def test_split_1(self):

        node = TextNode("This is text with a `code block` word", TextType.NORMAL_TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE_TEXT)
        expected_output = [
                            TextNode("This is text with a ", TextType.NORMAL_TEXT),
                            TextNode("code block", TextType.CODE_TEXT),
                            TextNode(" word", TextType.NORMAL_TEXT),
                        ]

        self.assertEqual(new_nodes, expected_output)



    def test_split_2(self):

        node = TextNode("This is text with a `code block` word", TextType.NORMAL_TEXT)
        node1 = TextNode("This is text with a `code block` word and a **bold text word** and an *italics* word.", TextType.NORMAL_TEXT)
        new_nodes = split_nodes_delimiter([node, node1], "`", TextType.CODE_TEXT)
        new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD_TEXT)
        new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC_TEXT)
        expected_output = [
                            TextNode("This is text with a ", TextType.NORMAL_TEXT),
                            TextNode("code block", TextType.CODE_TEXT),
                            TextNode(" word", TextType.NORMAL_TEXT),
                            TextNode("This is text with a ", TextType.NORMAL_TEXT),
                            TextNode("code block", TextType.CODE_TEXT),
                            TextNode(" word and a ", TextType.NORMAL_TEXT),
                            TextNode("bold text word", TextType.BOLD_TEXT),
                            TextNode(" and an ", TextType.NORMAL_TEXT),
                            TextNode("italics", TextType.ITALIC_TEXT),
                            TextNode(" word.", TextType.NORMAL_TEXT)
                        ]

        self.assertEqual(new_nodes, expected_output)

    # def test_split_3(self):

    #     node = TextNode("This is text with a **bolded *italicised `code block`*** word", TextType.NORMAL_TEXT)
    #     new_nodes = split_nodes_delimiter([node], "`", TextType.CODE_TEXT)
    #     new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD_TEXT)
    #     new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC_TEXT)
    #     expected_output = [
    #                         TextNode("This is text with a ", TextType.NORMAL_TEXT),
    #                         TextNode("code block", TextType.CODE_TEXT),
    #                         TextNode(" word", TextType.NORMAL_TEXT),
    #                     ]
    #     self.assertEqual(new_nodes, expected_output)

    def test_markdown_image(self):

        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected_out = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]

        self.assertEqual(expected_out, extract_markdown_images(text))

    def test_markdown_link(self):

        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        expected_out = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        
        self.assertEqual(expected_out, extract_markdown_links(text))

    def test_no_markdown_image(self):

        text = "This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected_out = []

        self.assertEqual(expected_out, extract_markdown_images(text)) 

    def test_no_markdown_link(self):

        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected_out = []

        self.assertEqual(expected_out, extract_markdown_links(text)) 

    def test_image_finder_1(self):

        node = TextNode(
                        "This is text with an image ![rick roll](https://i.imgur.com/aKaOqIh.gif) and a link [to youtube](https://www.youtube.com/@bootdotdev)",
                        TextType.NORMAL_TEXT,
        )
        new_nodes = split_nodes_image([node])
        expected_output = [
                            TextNode("This is text with an image ", TextType.NORMAL_TEXT),
                            TextNode("rick roll", TextType.IMAGES, "https://i.imgur.com/aKaOqIh.gif"),
                            TextNode(" and a link [to youtube](https://www.youtube.com/@bootdotdev)", TextType.NORMAL_TEXT)
                        ]

        self.assertEqual(new_nodes, expected_output)

    def test_image_finder_2(self):

        node = TextNode(
                        "This is text with an image ![rick roll](https://i.imgur.com/aKaOqIh.gif) and an image ![to youtube](https://www.youtube.com/@bootdotdev)",
                        TextType.NORMAL_TEXT,
        )
        new_nodes = split_nodes_image([node])
        expected_output = [
                            TextNode("This is text with an image ", TextType.NORMAL_TEXT),
                            TextNode("rick roll", TextType.IMAGES, "https://i.imgur.com/aKaOqIh.gif"),
                            TextNode(" and an image ", TextType.NORMAL_TEXT),
                            TextNode("to youtube", TextType.IMAGES, "https://www.youtube.com/@bootdotdev")
                             ]

        self.assertEqual(new_nodes, expected_output)

    def test_image_finder_3(self):

        node = TextNode(
                        "This is text with an image [rick roll](https://i.imgur.com/aKaOqIh.gif) and a link [to youtube](https://www.youtube.com/@bootdotdev)",
                        TextType.NORMAL_TEXT,
        )
        new_nodes = split_nodes_image([node])

        self.assertEqual(new_nodes, [node])

    def test_image_finder_4(self):

        node = TextNode(
                        "This is text with an image ![rick roll](https://i.imgur.com/aKaOqIh.gif) and a link [to youtube](https://www.youtube.com/@bootdotdev)",
                        TextType.BOLD_TEXT,
        )
        new_nodes = split_nodes_image([node])

        self.assertEqual(new_nodes, [node])

    def test_image_finder_5(self):

        node = TextNode(
                        "This is `text` with an image ![rick roll](https://i.imgur.com/aKaOqIh.gif) and *an* image ![to youtube](https://www.youtube.com/@bootdotdev) and some **baked beans** on top",
                        TextType.NORMAL_TEXT,
        )
        new_nodes = split_nodes_image([node])
        expected_output = [
                            TextNode("This is `text` with an image ", TextType.NORMAL_TEXT),
                            TextNode("rick roll", TextType.IMAGES, "https://i.imgur.com/aKaOqIh.gif"),
                            TextNode(" and *an* image ", TextType.NORMAL_TEXT),
                            TextNode("to youtube", TextType.IMAGES, "https://www.youtube.com/@bootdotdev"),
                            TextNode(" and some **baked beans** on top", TextType.NORMAL_TEXT)
                             ]

        self.assertEqual(new_nodes, expected_output)

    def test_image_finder_6(self):

        node = TextNode(
                        "![rick roll](https://i.imgur.com/aKaOqIh.gif)![to youtube](https://www.youtube.com/@bootdotdev)",
                        TextType.NORMAL_TEXT,
        )
        new_nodes = split_nodes_image([node])
        expected_output = [
                            TextNode("rick roll", TextType.IMAGES, "https://i.imgur.com/aKaOqIh.gif"),
                            TextNode("to youtube", TextType.IMAGES, "https://www.youtube.com/@bootdotdev")
                             ]

        self.assertEqual(new_nodes, expected_output)

    def test_link_finder_1(self):

        node = TextNode(
                        "This is text with an link [rick roll](https://i.imgur.com/aKaOqIh.gif) and an image ![to youtube](https://www.youtube.com/@bootdotdev)",
                        TextType.NORMAL_TEXT,
        )
        new_nodes = split_nodes_link([node])
        expected_output = [
                            TextNode("This is text with an link ", TextType.NORMAL_TEXT),
                            TextNode("rick roll", TextType.LINKS, "https://i.imgur.com/aKaOqIh.gif"),
                            TextNode(" and an image ![to youtube](https://www.youtube.com/@bootdotdev)", TextType.NORMAL_TEXT)
                        ]

        self.assertEqual(new_nodes, expected_output)

    def test_link_finder_2(self):

        node = TextNode(
                        "This is text with an image [rick roll](https://i.imgur.com/aKaOqIh.gif) and an image [to youtube](https://www.youtube.com/@bootdotdev)",
                        TextType.NORMAL_TEXT,
        )
        new_nodes = split_nodes_link([node])
        expected_output = [
                            TextNode("This is text with an image ", TextType.NORMAL_TEXT),
                            TextNode("rick roll", TextType.LINKS, "https://i.imgur.com/aKaOqIh.gif"),
                            TextNode(" and an image ", TextType.NORMAL_TEXT),
                            TextNode("to youtube", TextType.LINKS, "https://www.youtube.com/@bootdotdev")
                             ]

        self.assertEqual(new_nodes, expected_output)

    def test_link_finder_3(self):

        node = TextNode(
                        "This is text with an image ![rick roll](https://i.imgur.com/aKaOqIh.gif) and a link ![to youtube](https://www.youtube.com/@bootdotdev)",
                        TextType.NORMAL_TEXT,
        )
        new_nodes = split_nodes_link([node])

        self.assertEqual(new_nodes, [node])

    def test_link_finder_4(self):

        node = TextNode(
                        "This is text with an image ![rick roll](https://i.imgur.com/aKaOqIh.gif) and a link [to youtube](https://www.youtube.com/@bootdotdev)",
                        TextType.BOLD_TEXT,
        )
        new_nodes = split_nodes_link([node])

        self.assertEqual(new_nodes, [node])

    def test_link_finder_5(self):

        node = TextNode(
                        "This is `text` with an image [rick roll](https://i.imgur.com/aKaOqIh.gif) and *an* image [to youtube](https://www.youtube.com/@bootdotdev) and some **baked beans** on top",
                        TextType.NORMAL_TEXT,
        )
        new_nodes = split_nodes_link([node])
        expected_output = [
                            TextNode("This is `text` with an image ", TextType.NORMAL_TEXT),
                            TextNode("rick roll", TextType.LINKS, "https://i.imgur.com/aKaOqIh.gif"),
                            TextNode(" and *an* image ", TextType.NORMAL_TEXT),
                            TextNode("to youtube", TextType.LINKS, "https://www.youtube.com/@bootdotdev"),
                            TextNode(" and some **baked beans** on top", TextType.NORMAL_TEXT)
                             ]

        self.assertEqual(new_nodes, expected_output)

    def test_link_finder_6(self):

        node = TextNode(
                        "[rick roll](https://i.imgur.com/aKaOqIh.gif)[to youtube](https://www.youtube.com/@bootdotdev)",
                        TextType.NORMAL_TEXT,
        )
        new_nodes = split_nodes_link([node])
        expected_output = [
                            TextNode("rick roll", TextType.LINKS, "https://i.imgur.com/aKaOqIh.gif"),
                            TextNode("to youtube", TextType.LINKS, "https://www.youtube.com/@bootdotdev")
                             ]

        self.assertEqual(new_nodes, expected_output)

    def test_text_tonodes(self):

        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        expected_output = [
                            TextNode("This is ", TextType.NORMAL_TEXT),
                            TextNode("text", TextType.BOLD_TEXT),
                            TextNode(" with an ", TextType.NORMAL_TEXT),
                            TextNode("italic", TextType.ITALIC_TEXT),
                            TextNode(" word and a ", TextType.NORMAL_TEXT),
                            TextNode("code block", TextType.CODE_TEXT),
                            TextNode(" and an ", TextType.NORMAL_TEXT),
                            TextNode("obi wan image", TextType.IMAGES, "https://i.imgur.com/fJRm4Vk.jpeg"),
                            TextNode(" and a ", TextType.NORMAL_TEXT),
                            TextNode("link", TextType.LINKS, "https://boot.dev"),
                        ]

        self.assertEqual(text_to_textnodes(text), expected_output)

if __name__ == "__main__":
    unittest.main()