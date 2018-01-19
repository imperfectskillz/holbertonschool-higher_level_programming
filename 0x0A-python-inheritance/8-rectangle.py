#!/usr/bin/python3
"""
Module containing class Rec inherited from Base
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class Rect
    """
    def __init__(self, width, height):
        """
        Check using integer validator
        declare private in init
        """
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
