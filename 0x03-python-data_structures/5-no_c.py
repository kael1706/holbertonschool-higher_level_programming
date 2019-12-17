#!/usr/bin/python3
def no_c(my_string):
    a = list(my_string)
    for n_id, v in enumerate(a):
        if v == 'C' or v == 'c':
            del a[n_id]
    return "".join(a)
"""print(no_c("Holberton School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))
"""
