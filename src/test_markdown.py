
import unittest

from split_markdown import markdown_to_block, block_to_block_type

class TestSplitter(unittest.TestCase):
    def test_split_1(self):

        input = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.  \n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"

        output = markdown_to_block(input)

        expected_output = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
            ]

        self.assertEqual(output, expected_output)

    def test_blocker_1(self):
        input = "# This is a heading"
        output = block_to_block_type(input)
        expected_output = "h1"

        self.assertEqual(output, expected_output)

    def test_blocker_2(self):
        input = "### This is a heading"
        output = block_to_block_type(input)
        expected_output = "h3"

        self.assertEqual(output, expected_output)

    def test_blocker_3(self):
        input = "## T#his is a heading"
        output = block_to_block_type(input)
        expected_output = "h2"

        self.assertEqual(output, expected_output)

    def test_blocker_4(self):
        input = "###### T#his is a heading"
        output = block_to_block_type(input)
        expected_output = "h6"

        self.assertEqual(output, expected_output)

    def test_blocker_5(self):
        input = "```T#his is a code block```"
        output = block_to_block_type(input)
        expected_output = "code"

        self.assertEqual(output, expected_output)

    def test_blocker_6(self):
        input = "```T#his is not a code block heading``"
        output = block_to_block_type(input)
        expected_output = "p"

        self.assertEqual(output, expected_output)

    def test_blocker_7(self):
        input = ">T#his \n>is a quote \n>block```"
        output = block_to_block_type(input)
        expected_output = "blockquote"

        self.assertEqual(output, expected_output)

    def test_blocker_8(self):
        input = ">```T#his is not a \n>code block\n heading``"
        output = block_to_block_type(input)
        expected_output = "p"

        self.assertEqual(output, expected_output)

    def test_blocker_9(self):
        input = "* T#his \n* is an ul \n* >block```"
        output = block_to_block_type(input)
        expected_output = "ul"

        self.assertEqual(output, expected_output)

    def test_blocker_10(self):
        input = ">```T#his is not a \n>ul block\n heading``"
        output = block_to_block_type(input)
        expected_output = "p"

        self.assertEqual(output, expected_output)

    def test_blocker_11(self):
        input = "1. T#his \n2. is an ul \n3. >block```"
        output = block_to_block_type(input)
        expected_output = "ol"

        self.assertEqual(output, expected_output)

    def test_blocker_12(self):
        input = "1. >```T#his is not a \n2. ul block\n3.heading``"
        output = block_to_block_type(input)
        expected_output = "p"

        self.assertEqual(output, expected_output)

    def test_blocker_13(self):
        input = "1. >```T#his is not a \n2. ul block\n* .heading``"
        output = block_to_block_type(input)
        expected_output = "p"

        self.assertEqual(output, expected_output)

if __name__ == "__main__":
    unittest.main()