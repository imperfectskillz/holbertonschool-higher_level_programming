#!/usr/bin/python3
"""
module contains pascal traingle
"""


def pascal_triangle(n):
    """
    pascal triangle
    """
    if n <= 0:
        return []

    result = []
    for i in range(n):
        result.append([])
        result[i].append(1)
        for j in range(1, i):
            result[i].append(result[i - 1][j - 1] + result[i - 1][j])
        if (i > 0):
            result[i].append(1)

    return result
