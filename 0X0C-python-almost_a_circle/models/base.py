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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns JSON rep
        """
        if json_string is None or !(json_string):
            return '[]'
        return json.dumpts(list_dictionaries)

    @staticmethod
    def save_to_file(cls, list_objs):
        """
        writes list_objs to file
        """

    @staticmethod
    def from_json_string(json_string):
        """
        list from json
        """
        if json_string is None or !(json_string):
            return []
        return json.loads(json_string)
