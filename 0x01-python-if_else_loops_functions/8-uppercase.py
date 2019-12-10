#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        code = ord(letter)
        if code > 96 and code < 122:
            code = code - 32
            newletter = chr(code)
        else:
            newletter = letter
        print(newletter + "", end='')
    print("\n")
