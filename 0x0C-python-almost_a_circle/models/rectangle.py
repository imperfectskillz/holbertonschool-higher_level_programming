#!/usr/bin/python3
"""
This module contains the class Rectangle which inherits from base
"""
from models.base import Base


class Rectangle(Base):
    """
    class Rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes attributes
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        returns width
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        sets width
        """
        self.check('width', width)
        self.__width = width

    @property
    def height(self):
        """
        returns height
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        sets height
        """
        self.check('height', height)
        self.__height = height

    @property
    def x(self):
        """
        gets x
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        sets x
        """
        self.check('x', x)
        self.__x = x

    @property
    def y(self):
        """
        gets y
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        sets y
        """
        self.check('y', y)
        self.__y = y

    @staticmethod
    def check(name, value):
        """
        checks for int
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if (name == 'height' or name == 'width') and value <=0:
            raise ValueError("{} must be > 0".format(name))
        if (name == 'x' or name == 'y') and value < 0:
            raise ValueError("{} must be >= 0".format(name))

    def area(self):
        """
        returns area
        """
        return (self.width * self.height)

    def display(self):
        """
        prints ###
        """
        print('\n' * self.y, end='')
        for i in range(self.height):
            print(" " * self.x, end='')
            for j in range(self.width):
                print('#', end='')
            print()

    def __str__(self):
        """
        manual str rep
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """
        updates attributes
        """
        if args:
            try:
                for i in range(len(args)):
                    self.id = args[0]
                    self.width = args[1]
                    self.height = args[2]
                    self.x = args[3]
                    self.y = args[4]
            except IndexError:
                pass
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """
        dictionary rep
        """
        return ({'id': self.id, 'width': self.width, 'height': self.height, 'x': self.x, 'y': self.y})
