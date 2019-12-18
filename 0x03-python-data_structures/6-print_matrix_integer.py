#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            print("{:d}".format(matrix[r][c]), end=' ')
        print("")

"""matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
print_matrix_integer(matrix)
print("--")
print_matrix_integer()
"""
