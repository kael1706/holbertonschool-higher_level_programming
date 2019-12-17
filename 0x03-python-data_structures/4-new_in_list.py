#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list.copy()
    newCopy = my_list.copy()
    for n_id, v in enumerate(my_list):
        if n_id == idx:
            newCopy[n_id] = element
            return newCopy

"""my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)
"""
