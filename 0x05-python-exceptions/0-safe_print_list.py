#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    n_elements = 0
    for pos in range(x):
        try:
            print("{}".format(my_list[pos]), end="")
            n_elements = n_elements + 1
        except IndexError:
            continue
    print("")
    return n_elements
