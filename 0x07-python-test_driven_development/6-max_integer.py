#!/usr/bin/python3
"""
this is  a module 6-max-integer.

this module have the following functions:
max_integer: find and return the max integer
    in a list of integers.
    If the list is empty, the function returns None
"""


def max_integer(list=[]):
    """
    Find and return the max integer in a list of integers
    If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
