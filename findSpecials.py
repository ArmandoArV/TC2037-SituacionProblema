import re


def find_specials(text):
    return re.findall(r'(?<!["\'])\b([^\w\s])\b(?!["\'])', text)
