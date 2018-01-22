#!/usr/bin/python3
"""
module containing function that reads until give line number
"""


def read_lines(filename="", nb_lines=0):
    """
    prints given lines
    """
    i = 0
    with open(filename, encoding='utf-8') as a_file:
        if nb_lines <= 0:
            print(a_file.read(), end="")
        else:
            for line in a_file:
                while i < nb_lines:
                    print(line, end="")
                    i += 1
