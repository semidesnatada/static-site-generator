
from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode
from site_generation import copy_static, generate_page, generate_pages_recursively
import os

def main():
    print("Hello World")
    copy_static(os.path.join("src"))
    # generate_page(os.path.join("src/content/index.md"), os.path.join("src/template.html"), os.path.join("public/"))
    generate_pages_recursively(os.path.join("src/content"), os.path.join("src/template.html"), os.path.join("public"))

if __name__ == "__main__":
    main()
