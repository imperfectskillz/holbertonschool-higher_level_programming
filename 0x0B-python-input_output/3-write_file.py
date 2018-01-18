#!/usr/bin/python3
"""
Module containing function which writes to file
"""


def write_file(filename="", text=""):
    """
    WRites to file
    """
    with open(filename, mode='w', encoding='utf-8') as a_file:
        return a_file.write(text)
