#!/usr/bin/python3
def append_write(filename="", text=""):
    """
    append textat the end of a text file (UTF8)
    and returns the number of characters added:
    """
    n_ch = 0
    with open(filename, 'a+', encoding='utf-8') as f:
        n_ch = f.write(text)
    return n_ch
