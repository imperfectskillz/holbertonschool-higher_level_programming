#!/usr/bin/python3
"""
Module containing function which saves as json
"""
import json


def save_to_json_file(my_obj, filename):
    """
    saves as json
    """
    with open(filename, mode='w', encoding='utf-8') as a_file:
        a_file.write(json.dumps(my_obj))
