import re


def find_literals(text):
    return re.findall(r'\B(True|False|None|[-]?\d+[\.]?\d*)\B(?![\'"])', text)
