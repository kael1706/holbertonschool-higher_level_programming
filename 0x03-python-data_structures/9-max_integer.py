#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return(None)
    c_n = my_list[0]
    for n in my_list:
        if c_n < n:
            c_n = n
    return c_n

"""my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))
"""
