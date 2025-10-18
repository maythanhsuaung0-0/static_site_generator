import re


def extract_markdown_images(md):
    matches = re.findall(r"\!\[(.*?)\]+\((.*?)\)", md)
    return matches


def extract_markdown_links(md):
    matches = re.findall(r"\[(.*?)\]+\((.*?)\)", md)
    return matches


print(extract_markdown_images(
    "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png"))
