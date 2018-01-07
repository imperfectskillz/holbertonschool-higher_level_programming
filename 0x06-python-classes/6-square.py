#!/usr/bin/python3


class Square:
    """class Square defined"""

    def __init__(self, size=0, position=(0, 0)):
        """initializes size"""
        self.__size = size
        self.__position = position

    def area(self):
        """returns squared area"""
        squared = self.__size ** 2
        return squared

    @property
    def size(self):
        """getter for size"""
        return self.__size

    @size.setter
    def size(self, size):
        """setter for size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = size

    def my_print(self):
        """prints #"""
        if self.size > 0:
            for i in range(self.__position[0]):
                print("")
            for j in range(self.__size):
                print(" " * self.__position[0],  end="")
                print("#" * self.__size, end="")
                print("")
        else:
            print("")

    @property
    def position(self, value):
        """returns self position"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets position value"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position
