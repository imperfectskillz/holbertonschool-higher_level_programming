#!/usr/bin/python3
"""
Module contains class Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class Square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        initalizes above
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        manual string
        """
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """
        returns width
        """
        return self.width

    @size.setter
    def size(self, size):
        """
        sets width and height as size
        """
        self.check('width', size)
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """
        updates
        """
        if args and len(args) != 0:
            for i in range(len(args)):
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
        else:
            for k, v in kwars.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """
        dict rep
        """
        return ({'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y})
