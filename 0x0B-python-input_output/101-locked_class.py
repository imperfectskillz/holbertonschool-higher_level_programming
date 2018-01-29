#!/usr/bin/python3
"""
Module contains slots method
"""


class LockedClass():
    """
    Using slots to prevent user from creating more attributes
    """
    __slots__ = ["first_name"]
