#!/usr/bin/python3
"""
Module containing function that creates OBJ from json
MUST FIRST OPEN JSON FILE THEN LOAD
"""
import json


def load_from_json_file(filename):
    """
    creates obj from json
    """
    with open(filename) as a_file:
        return json.load(a_file)
