#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("{:s}".format("Last digit of " + str(number)), end='')
if number < 0:
    fix = -1
else:
    fix = 1
number = (abs(number) % 10) * fix
print("{:s}".format(" is " + str(number) + " and is "), end='')
if number > 5:
    print("greater than 5")
elif number is 0:
    print("0")
else:
    print("less than 6 and not 0")
