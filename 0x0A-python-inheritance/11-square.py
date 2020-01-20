#!/usr/bin/python3
"""
this is the module 10-square.
this module have the following classes:
Rectangle:
    area: return the area of rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class BaseGeometry"""

    def __init__(self, size):
        """
        reserved method that initialize
        the class attributes and methods
        """
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """return the area of the rectangle."""
        return self.__size ** 2

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
