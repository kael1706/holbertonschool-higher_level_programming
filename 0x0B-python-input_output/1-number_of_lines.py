#!/usr/bin/python3
def number_of_lines(filename=""):
    """ print the number of lines in the file"""
    n_lines = 0
    with open(filename, mode="r", encoding='utf-8') as f:
        info = f.readlines()
        n_lines = len(info)
    f.close()
    return n_lines
