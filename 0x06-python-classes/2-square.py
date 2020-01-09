#!/usr/bin/python3
class Square:
    """."""
    def __init__(self, size=0):
        """start of class"""
        try:
            self.__size = size
            if isinstance(size, int) == False:
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
