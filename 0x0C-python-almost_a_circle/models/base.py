#!/usr/bin/python3
"""
This module contains the class Base
"""
import json


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
        if not list_dictionaries or len(list_dictionaries) == 0:
            return '[]'
        return json.dumps(list_dictionaries)

    @staticmethod
    def save_to_file(cls, list_objs):
        """
        writes list_objs to file
        """
        result = []
        with open("{}.json".format(cls.__name__), "w") as a_file:
            if list_objs is None:
                a_file.write(Base.to_json_string(result)
            else:
                for thing in list_objs:
                    result.append(thing.to_dictionary())
                a_file.write(Base.to_json_string(result))

    @staticmethod
    def from_json_string(json_string):
        """
        list from json
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns instances with set attr
        """
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file_csv(cls):
        """
        returns list of instances
        """
        try:
            with open("{}.json".format(cls.__name__)) as a_file:
                things = Base.from_json_string(a_file.read())
                return ([cls.create(**obj) for obj in objs]
        except:
            return []
