#!/usr/bin/python3
"""
module containing function that returns number of lines of text file
"""


def number_of_lines(filename=""):
    """
    returns number of lines
    """
    line_number = 0
    with open(filename, encoding='utf-8') as a_file:
        for line in a_file:
            line_number += 1
    return line_number
