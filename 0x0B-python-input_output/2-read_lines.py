#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """read line by line according to the range"""
    n_lines = 0
    with open(filename, mode="r", encoding='utf-8') as f:
        info = f.readlines()
        if nb_lines == 0:
            nb_lines = len(info)
        for line in info:
            n_lines += 1
            if n_lines > nb_lines:
                break
            print(line, end="")
    f.close()
    return n_lines
