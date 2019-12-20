#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newD = {}
    for k, v in a_dictionary.items():
        newD[k] = a_dictionary[k] * 2
    return newD
"""
nF = '6-print_sorted_dictionary'
print_sorted_dictionary = __import__(nF).print_sorted_dictionary
a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
new_dict = multiply_by_2(a_dictionary)
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)"""
