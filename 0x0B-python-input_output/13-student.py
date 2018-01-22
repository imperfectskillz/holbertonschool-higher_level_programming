#!/usr/bin/python3
"""
Module containing class Student
"""


class Student:
    """
    Class student
    """
    def __init__(self, first_name, last_name, age):
        """
        Initalizes attributes
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        returns dict rep
        check for instance of list
        """
        if not isinstance(attrs, list):
            return self.__dict__

        """
        check for same key if given strings
        """
        result = {}
        for k in attrs:
            if k in self.__dict__:
                result[k] = self.__dict__[k]
        return result

    def reload_from_json(self, json):
        for k, v in json.items():
            self.__dict__[k] = v
