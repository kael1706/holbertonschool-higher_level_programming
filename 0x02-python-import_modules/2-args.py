#!/usr/bin/python3
import sys
if __name__ == '__main__':
    args = sys.argv
    del args[0]

    if not args:
        print("0 arguments.")
    else:
        print(str(len(args)) + " arguments:")
    for i, val in enumerate(args):
        print(i + 1, ": ", val)
