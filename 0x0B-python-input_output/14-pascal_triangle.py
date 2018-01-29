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
            a[i].append(a[i - 1][j - 1] + a[i - 1][j])
        if (n > 0):
            a[i].append(1)

    return result
