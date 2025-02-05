import unittest

from split_markdown import markdown_to_html_node

class TestEnsemble(unittest.TestCase):

    def test_example(self):

        input = "#### This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.  \n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        output = markdown_to_html_node(input)
        expected_output = "<div><h4>This is a heading</h4><p>This is a paragraph of text. It has some <b>bold</b> and <i>italic</i> words inside of it.</p><ul><li>This is the first list item in a list block</li><li>This is a list item</li><li>This is another list item</li></ul></div>"

        # print()
        # print("output to html")
        # print(output.to_html())
        # print()
        # print("expected output")
        # print(expected_output)
        # print()

        self.assertEqual(output.to_html(), expected_output)

    def test_example_1(self):

        input = '# Sample Markdown\n\nThis is some basic, sample markdown.\n\n## Second Heading\n\n* Unordered lists, and:\n\n1. One\n2. Two\n3. Three\n\n* More\n\n>Bloc**k**quote. chick\n> Beans\n\nAnd **bold**, *italics*. [A link](https://markdowntohtml.com) to somewhere.\n\n.\n\nOr an image of bears\n\n![bears](http://placebear.com/200/200)\n\nThe end ...'
        expected_output = '<div><h1>Sample Markdown</h1><p>This is some basic, sample markdown.</p><h2>Second Heading</h2><ul><li>Unordered lists, and:</li></ul><ol><li>One</li><li>Two</li><li>Three</li></ol><ul><li>More</li></ul><blockquote><p>Bloc<b>k</b>quote. chick</p><p> Beans</p></blockquote><p>And <b>bold</b>, <i>italics</i>. <a href="https://markdowntohtml.com">A link</a> to somewhere.</p><p>.</p><p>Or an image of bears</p><p><img src="http://placebear.com/200/200" alt="bears"></p><p>The end ...</p></div>'
        output = markdown_to_html_node(input).to_html()

        # print("output")
        # print(output)
        # print()
        # print("expected output")
        # print(expected_output)
        # print()

        self.assertEqual(output, expected_output)

if __name__ == "__main__":
    unittest.main()
