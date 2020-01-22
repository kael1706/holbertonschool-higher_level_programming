#!/usr/bin/python3
def write_file(filename="", text=""):
    """
    write a text and return the number of characters
    """
    n_characters = 0
    with open(filename, mode='w', encoding='UTF-8') as f:
        n_characters = f.write(text)
    return n_characters
