#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    if matrix:
        result = []
        for i in range(len(matrix)):
            result += [list(map((lambda x: x**2), matrix[i]))]
    return result
