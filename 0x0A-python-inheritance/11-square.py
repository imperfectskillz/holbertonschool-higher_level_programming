#!/usr/bin/python3
"""
Module containing class square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class Square
    """
    def __init__(self, size):
        """
        initiates private
        """
        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        """
        Area
        """
        return self.__size * self.__size

    def __str__(self):
        """
        string rep
        """
        return "[Square] {}/{}".format(self.__width, self.__height)
