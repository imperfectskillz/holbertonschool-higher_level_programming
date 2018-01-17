#!/usr/bin/python3
"""
Module containing class Mylist
"""


class MyList(list):
    """
    Inherits from list
    """
    def print_sorted(self):
        """
        prints sorted list
        """
        print(sorted(self))
