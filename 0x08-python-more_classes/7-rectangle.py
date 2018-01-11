#!/usr/bin/python3
"""
Module defines Rectangle class
"""


class Rectangle:
    """
    includes attributes for this class
    """
    number_of_instances = 0
    print_symbole = "#"

    def __init__(self, width=0, height=0):
        """initializes width and height"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """returns width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """returns height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns area of rectangle"""
        return self.width * self.height

    def perimeter(self):
        """returns perimeter of rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.width + self.height) * 2

    def __str__(self):
        """prints rectangle using #"""
        if self.width == 0 or self.height == 0:
            print()
        else:
            display = ""
            for i in range(self.height):
                for j in range(self.width):
                    display += self.print_symbol
                if i == self.height - 1:
                    continue
                else:
                    display += "\n"
            return display

    def __repr__(self):
        """prints string"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ Delete """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
