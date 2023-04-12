import re
from prettytable import PrettyTable


class Token:
    def __init__(self, token_type, lexeme):
        self.type = token_type
        self.lexeme = lexeme

    def __str__(self):
        return f"{self.type}: {self.lexeme}"


class Lexer:
    def __init__(self, input_string):
        self.input_string = input_string
        self.current_position = 0
        self.tokens = []

    def tokenize(self):
        while self.current_position < len(self.input_string):
            match = self.match_next()
            if match:
                token = Token(match["type"], match["lexeme"])
                self.tokens.append(token)
            else:
                self.current_position += 1
        return self.tokens

    def match_next(self):
        for matcher in matchers:
            match = matcher(self.input_string, self.current_position)
            if match:
                self.current_position += len(match["lexeme"])
                return match
        return None


def match_special(input_string, current_position):
    char = input_string[current_position]
    if char in specials:
        return {"type": "SPECIAL", "lexeme": char}
    return None


def match_operator(input_string, current_position):
    for operator in operators:
        if input_string.startswith(operator, current_position):
            return {"type": "OPERATOR", "lexeme": operator}
    return None


def match_literal(input_string, current_position):
    match = re.match(r'\B(True|False|None|[-]?\d+[\.]?\d*(?:[eE][-+]?\d+)?)\B(?![\'"])',
                     input_string[current_position:])
    if match:
        return {"type": "LITERAL", "lexeme": match.group()}
    return None


def match_keyword(input_string, current_position):
    match = re.match(
        r'\b(and|as|assert|break|class|continue|def|del|elif|else|except|exec|finally|for|from|global|if|import|in|is|lambda|not|or|pass|print|raise|return|try|while|with|yield)\b',
        input_string[current_position:])
    if match:
        return {"type": "KEYWORD", "lexeme": match.group()}
    return None


def match_identifier(input_string, current_position):
    match = re.match(
        r'(?<!["\'])\b(?!False|None|True|print|in|else|elif|if|range|for)([a-zA-Z_][a-zA-Z0-9_]*)\b(?!["\'])',
        input_string[current_position:])
    if match:
        return {"type": "IDENTIFIER", "lexeme": match.group()}
    return None


def match_delimiter(input_string, current_position):
    char = input_string[current_position]
    if char in delimiters:
        return {"type": "DELIMITER", "lexeme": char}
    return None


def match_comment(input_string, current_position):
    match = re.match(r'(?:(?<=^)|(?<=[^\w\s]))\#([^\n]*)', input_string[current_position:])
    if match:
        return {"type": "COMMENT", "lexeme": match.group()}
    return None


matchers = [
    match_special,
    match_operator,
    match_literal,
    match_keyword,
    match_identifier,
    match_delimiter,
    match_comment,
]

specials = {"(", ")", "[", "]", "{", "}", ",", ";", ":"}
operators = {"+", "-", "*", "/", "%", "**", "=", "=="}
delimiters = specials | operators | {" ", "\n", "\t", "\r"}


def print_table(data):
    max_lexeme_length = max([len(row[1]) for row in data])
    data = [row for row in data if row[1].strip()]
    # Print table header
    print("+------------+{}+------------+".format("-" * max_lexeme_length))
    print("| Token Type | Lexeme        |".format(" " * max_lexeme_length))
    print("+------------+{}+------------+".format("-" * max_lexeme_length))

    # Print table rows
    for row in data:
        token_type = row[0].ljust(11)
        lexeme = row[1].ljust(max_lexeme_length)
        print("| {}| {} |".format(token_type, lexeme))

    # Print table footer


if __name__ == "__main__":
    input_string = '''b=7
        a = 32.4 *(-8.6 - b)/       6.1E-8
        d = a ^ b # Esto es un comentario
    '''
    lexer = Lexer(input_string)
    tokens = lexer.tokenize()

    # Convert list of tokens to list of tuples
    token_tuples = [(token.type, token.lexeme) for token in tokens]

    # Print pretty table
    print_table(token_tuples)
