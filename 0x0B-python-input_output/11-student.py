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

    def to_json(self):
        """
        returns dict rep
        """
        return self.__dict__
