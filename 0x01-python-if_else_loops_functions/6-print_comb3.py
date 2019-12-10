#!/usr/bin/python3
for first in range(10):
    for second in range(10):
        if first < second and first != 8 and second != 9:
            print("{:d}{:d}".format(first, second), end=', ')
        elif first == 8 and second == 9:
            print("{:d}{:d}".format(first, second), sep='')
