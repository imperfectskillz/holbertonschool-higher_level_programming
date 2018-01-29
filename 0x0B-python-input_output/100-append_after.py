#!/usr/bin/python3
"""
Module contains append_after
"""


def append_after(filename="", search_string="", new_string=""):
    """
    if search_string exists, replace with new_string
    """
    temp = ""
    with open(filename, "r", encoding="utf-8") as opened_file:
        for line in opened_file:
            temp += line
            if search_string in line:
                temp += new_string
    with open(filename, "w", encoding="utf-8") as opened_file:
        opened_file.write(temp)
