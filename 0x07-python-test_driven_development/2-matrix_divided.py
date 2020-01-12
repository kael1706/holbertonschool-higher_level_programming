#!/usr/bin/python3
"""
this is the module 2-matrix_divided.
this module have the following functions:
matrix_divided: divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.
    """
    e_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if isinstance(matrix, list) is False or matrix is None:
        raise TypeError(e_msg)
    for r in matrix:
        if isinstance(r, list) is False:
            raise TypeError(e_msg)
        for c in r:
            if isinstance(c, (int, float)) is False:
                raise TypeError(e_msg)
    for r in matrix:
        if len(matrix[0]) != len(r):
            raise TypeError("Each row of the matrix must have the same size")
    if isinstance(div, (int, float)) is False:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    newM = list(map(list, matrix))
    for idx1, r in enumerate(matrix):
        for idx2, c in enumerate(r):
            newM[idx1][idx2] = round(c / div, 2)
    return newM
