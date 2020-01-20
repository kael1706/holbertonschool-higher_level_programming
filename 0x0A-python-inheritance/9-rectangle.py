#!/usr/bin/python3
"""
this is the module 9-rectangle.
this module have the following classes:
Rectangle:
    area: return the area of rectangle
    __str__: print
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

    def area(self):
        """return the area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
