import re


def find_identifiers(text):
    # Use a negative lookbehind to exclude identifiers within quotes
    return re.findall(r'(?<!["\'])\b([a-zA-Z_][a-zA-Z0-9_]*)\b(?!["\'])', text)
