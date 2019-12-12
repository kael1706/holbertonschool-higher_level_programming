#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    from calculator_1 import add, sub, mul, div

    args = sys.argv
    del args[0]
    if not args or len(args) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(args[0])
    o = str(args[1])
    b = int(args[2])
    if o == "+":
        print("{} {} {} = {}".format(a, o, b, add(a, b)))
    elif o == "-":
        print("{} {} {} = {}".format(a, o, b, sub(a, b)))
    elif o == "*":
        print("{} {} {} = {}".format(a, o, b, mul(a, b)))
    elif o == "/":
        print("{} {} {} = {}".format(a, o, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
