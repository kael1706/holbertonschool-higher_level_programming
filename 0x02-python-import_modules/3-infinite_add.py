#!/usr/bin/python3
import sys
if __name__ == '__main__':
    args = sys.argv
    del args[0]
    answer = 0
    for n in args:
        answer = answer + int(n)
    print(answer)
