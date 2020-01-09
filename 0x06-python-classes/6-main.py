#!/usr/bin/python3
Square = __import__('6-square').Square

my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")
"""

my_square_4 = Square(-3)
my_square_4.my_print()

print("--")

my_square_4 = Square(4, (-1, 0))
my_square_4.my_print()

print("--")

my_square_4 = Square(5, (0, -1))
my_square_4.my_print()

print("--")

my_square_4 = Square(6, ("a", 0))
my_square_4.my_print()

print("--")

my_square_4 = Square(7, (0, "e"))
my_square_4.my_print()

print("--")

my_square_4 = Square(3, ("a", "b"))
my_square_4.my_print()

print("--")
"""
