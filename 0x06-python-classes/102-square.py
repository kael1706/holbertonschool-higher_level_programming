#!/usr/bin/python3
class Square:
    """class square."""
    def __init__(self, size=0):
        """start of class."""
        self.__size = size

    @property
    def size(self):
        """get the size."""
        return self.__size

    @size.setter
    def size(self, size):
        """set the size."""
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """public instance method."""
        return self.__size ** 2

    def __eq__(self, other):
        """comparing myself to someone similar to me."""
        return self.__size == other.__size

    def __ne__(self, other):
        """comparing."""
        return self.__size != other.__size

    def __gt__(self, other):
        """comparing."""
        return self.__size > other.__size

    def __ge__(self, other):
        """comparing."""
        return self.__size >= other.__size

    def __lt__(self, other):
        """comparing."""
        return self.__size < other.__size

    def __le__(self, other):
        """comparing."""
        return self.__size <= other.__size
