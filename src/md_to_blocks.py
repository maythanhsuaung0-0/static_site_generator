import re


def markdown_to_blocks(md):
    md_list = md.split("\n\n")
    for block in md_list:
        block = block.strip()
    return md_list


markdown_to_blocks(
    "# Heading 1\n\nThis is a paragraph with **bold** text and _italic_ text.\n\n- List item 1\n- List item 2")
