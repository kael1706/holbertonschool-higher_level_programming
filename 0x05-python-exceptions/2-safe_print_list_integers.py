#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    n_elements = 0
    for pos in range(x):
        if pos <= x:
            try:
                print("{:d}".format(my_list[pos]), end="")
                n_elements = n_elements + 1
            except (TypeError, ValueError):
                pass
    print("")
    return n_elements
