#!/usr/bin/python3
"""
this is the module base.
this module has the followings classes:
base.
"""


class Base():
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize attributes"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
