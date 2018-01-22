#!/usr/bin/python3
"""
module containing function that reads and prints file
"""


def read_file(filename=""):
    """
    prints content of file
    """
    with open(filename, encoding='utf-8') as a_file:
        print(a_file.read(), end="")
