#!/usr/bin/python3
"""
this is the class Rectangle.
"""


class Rectangle():
    """class"""
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        get width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        set width.
        """
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        get height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        set height.
        """
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Public instance method
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Public instance method
        """
        if self.__width is 0 or self.__height is 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Instance method that returns an “informal”
        and nicely printable string representation
        of an instance
        """
        if self.width is 0 or self.height is 0:
            return ""
        rect_draw = []
        for row in range(self.__height):
            for col in range(self.__width):
                rect_draw.append('#')
            rect_draw.append('\n')
        rect = "".join(rect_draw)
        return rect[:-1]
    def __del__(self):
        """Instance method called when an instance is deleted"""
        print("Bye rectangle...")
