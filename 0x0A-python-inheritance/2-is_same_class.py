#!/usr/bin/python3
"""
this is the module 1-is_same_class.
this module have the following functions:
is_same_class:
"""


def is_same_class(obj, a_class):
    """function"""
    if type(obj) is a_class:
        return True
    else:
        return False
