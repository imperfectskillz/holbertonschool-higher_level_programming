#!/usr/bin/python3
"""
Module contains BaseGeometry class
"""


class BaseGeometry:
    """
    Class now contains area function
    """
    def area(self):
        """
        area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        checks value to see if integer
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
