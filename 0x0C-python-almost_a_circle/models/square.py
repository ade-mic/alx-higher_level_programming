#!/usr/bin/python3
"""
This file contaiins a class called Square which is a child of Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square is a class that is inherited from Rectangle
    Method:
        __init__: class constructor
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Class Constructor
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return '[{}] ({}) {}/{} - {}'.format(type(self).__name__,
                                             self.id, self.x,
                                             self.y, self.width)

    @property
    def size(self):
        """
        gets the value of size
        """
        return self.width
    
    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
