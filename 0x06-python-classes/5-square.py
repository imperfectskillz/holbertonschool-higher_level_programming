#!/usr/bin/python3


class Square:
    """class Square defined"""

    def __init__(self, size=0):
        """initializes size"""
        self.__size = size

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
            for i in range(self.size):
                for j in range(self.size):
                    print("#", end=" ")
                print("")
        else:
            print("")
