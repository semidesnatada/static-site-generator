
from textnode import TextType, TextNode

import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):

    out = []

    for node in old_nodes:
        if node.text_type != TextType.NORMAL_TEXT:
            out.append(node)
        else:
            out_nest = []

            chunks = node.text.split(delimiter)
            if len(chunks) % 2 == 0:
                raise Exception(f"Invalid markdown: {delimiter} was not closed / opened.")
            else:
                for i, chunk in enumerate(chunks):
                    if i % 2 == 0:
                        out.append(TextNode(chunk, TextType.NORMAL_TEXT))
                    else:
                        out.append(TextNode(chunk, text_type))

            out.extend(out_nest)
    return out

def extract_markdown_images(text):

    search = re.findall(r"(!\[.*?\]\(.*?\))", text)
    output = []
    for match in search:
        output.append((match.partition(']')[0].partition('[')[-1],
                       match.partition(')')[0].partition('(')[-1]))

    return output

def extract_markdown_links(text):

    search = re.findall(r"(?<!!)(\[.*?\]\(.*?\))", text)
    output = []
    for match in search:
        output.append((match.partition(']')[0].partition('[')[-1],
                       match.partition(')')[0].partition('(')[-1]))

    return output

def split_nodes_image(old_nodes):

    out = []
    for node in old_nodes:
        #Don't process if it isn't a normal text node
        if node.text_type != TextType.NORMAL_TEXT:
            out.append(node)
        else:
            out_nest = []
            find_image = extract_markdown_images(node.text)
            #Don't bother processing if there are no image tags inside
            if not find_image:
                out_nest.append(node)
            else:
                remaining_node_text = node.text
                for image_tuple in find_image:
                    #split the input text along the specific image
                    chunks = remaining_node_text.split(f"![{image_tuple[0]}]({image_tuple[1]})", 1)
        
                    #If there is content before the image tag, then add it as a text node
                    if chunks[0]:
                        out_nest.append(TextNode(chunks[0], TextType.NORMAL_TEXT))
                    #add the image tag as an image node
                    out_nest.append(TextNode(image_tuple[0], TextType.IMAGES, image_tuple[1]))

                    #reset the remaining node text to be processed
                    remaining_node_text = chunks[1]

                #if after the loop has completed there remains any further text, add it to a final textnode.
                if remaining_node_text:
                    out_nest.append(TextNode(remaining_node_text,TextType.NORMAL_TEXT))

            out.extend(out_nest)
    return out

def split_nodes_link(old_nodes):
    """This function has identical structure to split_nodes_image."""
    out = []
    for node in old_nodes:
        #Don't process if it isn't a normal text node
        if node.text_type != TextType.NORMAL_TEXT:
            out.append(node)
        else:
            out_nest = []
            find_link = extract_markdown_links(node.text)
            #Don't bother processing if there are no image tags inside
            if not find_link:
                out_nest.append(node)
            else:
                remaining_node_text = node.text
                for link_tuple in find_link:
                    #split the input text along the specific link
                    chunks = remaining_node_text.split(f"[{link_tuple[0]}]({link_tuple[1]})", 1)
        
                    #If there is content before the image tag, then add it as a text node
                    if chunks[0]:
                        out_nest.append(TextNode(chunks[0], TextType.NORMAL_TEXT))
                    #add the image tag as an image node
                    out_nest.append(TextNode(link_tuple[0], TextType.LINKS, link_tuple[1]))

                    #reset the remaining node text to be processed
                    remaining_node_text = chunks[1]

                #if after the loop has completed there remains any further text, add it to a final textnode.
                if remaining_node_text:
                    out_nest.append(TextNode(remaining_node_text,TextType.NORMAL_TEXT))

            out.extend(out_nest)
    return out

def text_to_textnodes(text):

    delimiters = {"`":TextType.CODE_TEXT,
                  "**":TextType.BOLD_TEXT,
                  "*":TextType.ITALIC_TEXT}

    initial_node = [TextNode(text, TextType.NORMAL_TEXT)]
    inter_nodes_1 = split_nodes_link(initial_node)
    inter_nodes_2 = split_nodes_image(inter_nodes_1)
    
    for delimiter, text_type in delimiters.items():
        inter_nodes_2 = split_nodes_delimiter(inter_nodes_2, delimiter, text_type)

    inter_nodes_3 = []

    for node in inter_nodes_2:
        if node.text:
            inter_nodes_3.append(node)

    return inter_nodes_3