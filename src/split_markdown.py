
from htmlnode import ParentNode, LeafNode, HTMLNode
from split_nodes import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType

def markdown_to_block(markdown):
    out=[]
    chunks = markdown.split("\n\n")
    for chunk in chunks:
        if chunk:
            out.append(chunk.strip())

    return out

def block_to_block_type(markdown_block):

    if markdown_block[0] == "#":
        count = 1
        for character in markdown_block[1:6]:
            if character == "#":
                count += 1
            else:
                break
        return f"h{count}"

    if markdown_block[:3] == "```" and markdown_block[-3:] == "```":
        return "code"

    lines = markdown_block.split("\n")

    is_quote = True
    is_ul = True
    is_ol = True

    for i, line in enumerate(lines):
        if line[0] != ">":
            is_quote = False
        if line[:2] != "- " and line[:2] != "* ":
            is_ul = False
        #support ordered lists of up to 99 elements
        if i <= 8:
            if line[:3] != f"{i+1}. ":
                is_ol = False
        elif i > 8:
            if line[:4] != f"{i+1}. ":
                is_ol = False
        if not is_quote and not is_ul and not is_ol:
            return "p"
    
    if is_quote:
        return "blockquote"
    if is_ul:
        return "ul"
    if is_ol:
        return "ol"

def markdown_lists_to_html(markdown_block, block_tag):
    list_children = []
    list_items = markdown_block.split("\n")
    for list_item in list_items:
        if block_tag == "ul":
            text = list_item[2:]
        else:
            text = list_item[3:]
        text_children = text_to_textnodes(text)
        html_children = []
        for text_child in text_children:
            # html_children.append(ParentNode("span", [text_node_to_html_node(text_child)]))
            html_children.append(text_node_to_html_node(text_child))
        list_children.append(ParentNode("li", html_children))

    return ParentNode(tag=block_tag, children=list_children)

def markdown_header_to_html(markdown_block, block_type):
    trimmed_content = markdown_block[int(block_type[1:])+1:]
    text_nodes = text_to_textnodes(trimmed_content)
    html_nodes = []
    for text_node in text_nodes:
        html_nodes.append(text_node_to_html_node(text_node))
    return ParentNode(tag = block_type, children = html_nodes)

def markdown_para_to_html(markdown_block):
    children_textnodes = text_to_textnodes(markdown_block)
    children_htmlnodes = []
    for text_node in children_textnodes:
        children_htmlnodes.append(text_node_to_html_node(text_node))
    return ParentNode(tag="p", children = children_htmlnodes)

def markdown_code_to_html(markdown_block, block=False):
    children_textnode = TextNode(markdown_block[3:-3], TextType.CODE_BLOCK)
    htmlnodes = text_node_to_html_node(children_textnode)
    return htmlnodes

def markdown_blockquote_to_html(markdown_block):
    list_children = []
    list_items = markdown_block.split("\n")
    for list_item in list_items:
        text = list_item[2:]
        text_children = text_to_textnodes(text)
        html_children = []
        for text_child in text_children:
            html_children.append(text_node_to_html_node(text_child))

        list_children.extend(html_children)
    return ParentNode(tag="blockquote", children=list_children)

def markdown_to_html_node(markdown):
    
    markdown_blocks = markdown_to_block(markdown)
    block_html_nodes = []

    for markdown_block in markdown_blocks:
        block_type = block_to_block_type(markdown_block)
        if block_type == "p":
            block_html_nodes.append(markdown_para_to_html(markdown_block))
        elif block_type == "ul" or block_type == "ol":
            block_html_nodes.append(markdown_lists_to_html(markdown_block, block_type))
        elif block_type == "code":
            block_html_nodes.append(markdown_code_to_html(markdown_block, block=True))
        elif block_type[0] == "h":
            block_html_nodes.append(markdown_header_to_html(markdown_block, block_type))
        elif block_type == "blockquote":
            block_html_nodes.append(markdown_blockquote_to_html(markdown_block))

    return ParentNode(tag="div", children=block_html_nodes)

def extract_title(markdown):

    lines = markdown.split("\n")
    
    for line in lines:
        if line[:2] == "# ":
            return line[2:]
    raise Exception("Doc has no title")