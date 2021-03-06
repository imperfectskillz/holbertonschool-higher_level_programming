#!/usr/bin/python3
"""
function that prints a square with #
"""


def print_square(size):
    """
    size is length of square
    """
    i = 0
    j = 0
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print()

    while i < size:
        print("#" * size, end="")
        print()
        i += 1
