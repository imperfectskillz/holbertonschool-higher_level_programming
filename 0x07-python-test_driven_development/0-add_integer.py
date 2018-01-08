#!/usr/bin/python3
"""
defines function that adds two ints and returns result
"""


def add_integer(a, b):
    """
    returns sum of a and b
    both must be integers otherwise throws a TypeError
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
