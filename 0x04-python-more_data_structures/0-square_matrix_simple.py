#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newM = list(map(list, matrix))
    for r, vr in enumerate(matrix):
        for c, vc in enumerate(vr):
            newM[r][c] = newM[r][c] ** 2
    return newM
"""matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
new_matrix = square_matrix_simple(matrix)
print(new_matrix)
priint(matrix)
"""
