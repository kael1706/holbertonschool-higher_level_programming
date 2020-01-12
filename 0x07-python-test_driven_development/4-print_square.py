#!/usr/bin/bash
"""
this is the module 4-print_square.
this module have the following functions:
print_square: prints a square with the character
"""


def print_square(size):
    if isinstance(size, int) is False and\
            isinstance(size, float) is False:
                raise TypeError("size must be an integer")
    if isinstance(size, float) is True and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for a in range(0, int(size)):
        for b in range(0, int(size)):
            print("#", end="")
        print("")
