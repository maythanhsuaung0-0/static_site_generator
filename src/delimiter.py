import re
from extract import extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType


def split_nodes_delimiter(old_node, delimiter, text_type):
    new_list = []
    if (old_node.text_type != TextType.TEXT):
        new_list.append(old_node)
        return new_list
    splitted = old_node.text.split(delimiter)
    if len(splitted) % 2 == 0:
        raise Exception("Not a valid Markdown syntax")
    for i in range(len(splitted)):
        node = ''
        if i % 2 == 0:
            node = TextNode(splitted[i], TextType.TEXT)
        else:
            node = TextNode(splitted[i], text_type)
        new_list.append(node)
    return new_list


split_nodes_delimiter(TextNode("this is **bold** text",
                      TextType.TEXT), '**', 'bold')


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if (old_node.text_type != TextType.TEXT):
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            print(f"separated {sections}")
            if len(sections) != 2:
                raise ValueError(
                    "invalid markdown syntax, image section is not close")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes


def split_nodes_links(old_notes):
    new_nodes = []
    for old_node in old_notes:
        if (old_node.text_type != TextType.TEXT):
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})")
            if len(sections) != 2:
                raise ValueError("Invalid syntax, link section is not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes
