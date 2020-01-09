#!/usr/bin/python3
class Square:
    """class square"""
    def __init__(self, size=0, position=(0, 0)):
        """start of class"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """get the size"""
        return self.__size

    @size.setter
    def size(self, size):
        """set the size"""
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """public instance method"""
        return self.__size ** 2

    def my_print(self):
        """print a square"""
        for y in range(0, self.__position[1]):
            print("")
        for a in range(0, self.__size):
            for x in range(0, self.__position[0]):
                print(" ", end="")
            for b in range(0, self.__size):
                print("#", end="")
            print("")
        if (self.__size <= 0):
            print("")

    @property
    def position(self):
        """get the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """set the position"""
        if isinstance(value, tuple) is False or\
                len(value) != 2 or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
