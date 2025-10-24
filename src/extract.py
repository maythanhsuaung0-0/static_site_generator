import re


def extract_markdown_images(md):
    matches = re.findall(r"\!\[(.*?)\]+\((.*?)\)", md)
    return matches


def extract_markdown_links(md):
    matches = re.findall(r"\[(.*?)\]+\((.*?)\)", md)
    return matches


def extract_markdown_lists(md):
    matches = re.findall(r"\-(.*?)", md)
    return matches


def extract_markdown_heading(md):
    matches = re.findall(r"\#(.*?)", md)
    return matches


