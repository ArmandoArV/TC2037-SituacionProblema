import re


def find_comments(text):
    return re.findall(r'(?<!["\'])\#([^\n]*)', text)
