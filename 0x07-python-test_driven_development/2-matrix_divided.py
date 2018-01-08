#!/usr/bin/python3
"""
Matrix divided by div and returns new list
"""


def matrix_divided(matrix, div):
    """matrix divided by div"""
    result = []
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    return [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
