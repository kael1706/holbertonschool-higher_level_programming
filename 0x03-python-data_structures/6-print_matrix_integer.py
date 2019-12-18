#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for r, vr in enumerate(matrix):
        for c, vc in enumerate(vr):
            if c == len(matrix[r]) - 1:
                print("{:d}".format(matrix[r][c]), end='')
            else:
                print("{:d}".format(matrix[r][c]), end=' ')
        print("{:s}".format(''))
"""matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print_matrix_integer(matrix)
print("--")
print_matrix_integer()
"""
