#!/usr/bin/python3
"""
This module contains the class Base
"""


class Base:
    """
    original class to work with
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        init
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """
        returns JSON rep
        """
        if json_string is None or !(json_string):
            return list
        return json.dumpts(list_dictionaries)

    def save_to_file(cls, list_objs):
        """
        writes list_objs to file
        """
        
