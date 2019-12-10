#!/usr/bin/python3
def uppercase(str):
    for pos in range(0, len(str)):
        code = ord(str[pos])
        if code > 96 and code < 122:
            code = code - 32
        print("{:s}".format(chr(code)), end='')
    print("{:s}".format('\n'))
