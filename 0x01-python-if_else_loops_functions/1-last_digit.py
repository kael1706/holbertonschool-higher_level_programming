#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of " + str(number), end='')
if number < 0:
     fix = -1
else:
     fix = 1
number = abs(number) % 10
print(" is " + str(number * fix) + " and is ", end='')
if number > 5:
    print("greater than 5")
elif number is 0:
    print("0")
else:
    print("less than 6 and not 0")
