#!/usr/bin/python3
import sys
if __name__ == '__main__':
    args = sys.argv
    del args[0]

    if not args:
        print("0 arguments.")
    elif len(args) is 1:
        print("1 argument:")
    else:
        print(str(len(args)) + " arguments:")
    for i, val in enumerate(args):
        print("{}: {}".format(i+1, val))
