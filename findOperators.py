import re


def find_operators(text):
    return re.findall(r'\B(\+|\-|\*|\/|\%|\*\*|\=|\==)\B', text)
