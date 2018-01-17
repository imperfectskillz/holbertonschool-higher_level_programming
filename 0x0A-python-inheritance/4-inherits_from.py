#!/usr/bin/python3
"""
Module contains method to check inheritance
"""


def inherits_from(obj, a_class):
    """
    returns true or false after checking if subclass or not
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
