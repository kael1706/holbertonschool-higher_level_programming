#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_list = list(set(my_list))
    c = 0
    for item in my_list:
        c = c + item
    return c
"""
my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print("Result: {:d}".format(result))
"""
