#!/usr/bin/python3
"""
this is the module 0-add_integer.

this module have the following functions:
0-add_integer: add two integer numbers.
"""


def add_integer(a, b=98):
    """
    Add two integer numbers.
    """
    if isinstance(a, int) is False and\
            isinstance(a, float) is False:
        raise TypeError("a must be an integer")
    if isinstance(b, (int, float)) is False:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
