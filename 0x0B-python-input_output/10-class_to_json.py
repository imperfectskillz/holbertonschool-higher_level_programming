#!/usr/bin/python3
"""
Module contains function that returns the dict description
"""


def class_to_json(obj):
    """
    REturns dict
    """
    return obj.__dict__
