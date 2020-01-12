#!/usr/bin/python3
"""
this is the module 3-say_my_name.
this module have the following functions:
say_my_name: print My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    Prints My name is <first name> <last name>
    """
    e_msj = "first_name must be a string"
    if first_name is None:
        raise TypeError(e_msj)
    if isinstance(first_name, str) is False:
        raise TypeError(e_msj)
    if isinstance(last_name, str) is False:
        raise TypeError("last_name" + e_msj[-17:])
    print("My name is {:s} {:s}".format(first_name, last_name))
