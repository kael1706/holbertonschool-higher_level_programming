#!/usr/bin/python3
"""
this is the module 0-lookup.
this module have the following functions:
lookup: return the dir of object.
"""


def lookup(obj):
    """dir of object"""
    infoObj = dir(obj)
    return list(infoObj)
