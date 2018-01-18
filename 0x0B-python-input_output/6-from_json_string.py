#!/usr/bin/python3
"""
Module containing function returning json obj
"""
import json


def from_json_string(my_str):
    """
    returns json rep
    """
    return json.loads(my_str)
