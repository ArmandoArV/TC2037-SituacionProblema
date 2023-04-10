import re


def find_delimiters(text):
    return re.findall(r'\B([\(\)\[\]\{\}\,\:\.])\B', text)
