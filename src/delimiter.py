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
