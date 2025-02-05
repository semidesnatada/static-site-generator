
from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
    print("Hello World")


    tester1 = "`bea`hel`lo`ns"
    tester2 = "b`ea`hel`lo`ns"

    print(tester1.split("`"))
    print(tester2.split("`"))

    for chunk in tester1.split("`"):
        if chunk:
            print(chunk)

    text_node1 = TextNode("Baked Beans", TextType.NORMAL_TEXT)
    text_node2 = TextNode("This is not a text node", TextType.LINKS, "great-web-com")
    print(text_node1)

    converted1 = text_node_to_html_node(text_node1)
    print(converted1)

    print(text_node2)

    converted2 = text_node_to_html_node(text_node2)
    print(converted2)

    # html_node_0 = HTMLNode(None, "Press this to go to google", None, None)
    # html_node_1 = HTMLNode("p", "Hello mr. beans", None, None)
    # html_node_2 = HTMLNode("a", None, html_node_0, {"href": "https://www.google.com"})
    # print(html_node_0)
    # print(html_node_1)
    # print(html_node_2)
    # print(html_node_2.props_to_html())

    # leaf_2 = LeafNode("a", "Click me!", props={"href": "https://www.google.com"})
    # print('<a href="https://www.google.com">Click me!</a>')
    # print(leaf_2.to_html())
    # print(leaf_2)

    # node = ParentNode(
    #                     "p",
    #                     [
    #                         LeafNode("b", "Bold text"),
    #                         LeafNode(None, "Normal text"),
    #                         LeafNode("i", "italic text"),
    #                         LeafNode(None, "Normal text"),
    #                     ]
    #                 )

    # x = node.to_html()
    # print(x)

if __name__ == "__main__":
    main()
