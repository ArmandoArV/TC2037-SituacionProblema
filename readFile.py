def read_file(file_name):
    with open(file_name, 'r') as file:
        text = file.read()
    return text
