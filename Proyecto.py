from findComments import find_comments
from findDelimiters import find_delimiters
from findIdentifiers import find_identifiers
from findKeyWords import find_keywords
from findLiterals import find_literals
from findOperators import find_operators
from findSpecials import find_specials
from generateHTML import generate_html_output
from readFile import read_file
from writeFile import write_html_file


def main():
    file_name = '/media/armando/Data/TC2037/SituacionProblemaPython/TestFIle.txt'
    html_file_name = 'main.html'
    text = read_file(file_name)
    token_list = []
    token_list += [(value, 'identifier') for value in find_identifiers(text)]
    token_list += [(value, 'keyword') for value in find_keywords(text)]
    token_list += [(value, 'operator') for value in find_operators(text)]
    token_list += [(value, 'delimiter') for value in find_delimiters(text)]
    token_list += [(value, 'literal') for value in find_literals(text)]
    token_list += [(value, 'special-symbol') for value in find_specials(text)]
    token_list += [(value, 'comment') for value in find_comments(text)]
    token_list.sort(key=lambda x: text.find(x[0]))
    html_output = generate_html_output(text, token_list)
    write_html_file(html_output, html_file_name)


if __name__ == '__main__':
    main()
