#!/usr/bin/python3
"""
Module containing class MyList
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
