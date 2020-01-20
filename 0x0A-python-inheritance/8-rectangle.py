#!/usr/bin/python3
"""
this is the module 8-rectangle.
this module have the following classes:
Rectangle.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class BaseGeometry"""

    def __init__(self, width, height):
        """
        reserved method that initialize
        the class attributes and methods
        """
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
