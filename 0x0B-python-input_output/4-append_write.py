#!/usr/bin/python3
"""
Module contains function that appends to text file
"""


def append_write(filename="", text=""):
    """
    appends to the file
    must set mode to a for append
    """
    with open(filename, mode='a', encoding='utf-8') as a_file:
        return a_file.write(text)
