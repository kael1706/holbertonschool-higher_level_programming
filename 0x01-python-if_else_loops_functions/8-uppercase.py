#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        code = ord(letter)
        if code > 97 and code < 122:
            code = code - 32
            print(chr(code) + "")
        else:
            print(letter + "")
