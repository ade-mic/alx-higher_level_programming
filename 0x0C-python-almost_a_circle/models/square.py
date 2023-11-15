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
    """
    set the value of size
    """
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates the trribute of the class of square
        Args:
            *args positional arguement
            1st argument should be the id attribute
            2nd argument should be the size attribute
            3rd argument should be the x attribute
            4th argument should be the y attribute
        Kwargs - key word arguements(optional):
        """
        if args:
            if len(args) == 1:
                self.id = args[0]
            elif len(args) == 2:
                self.id = args[0]
                self.size = args[1]
            elif len(args) == 3:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
            elif len(args) == 4:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
        if args and len(args) != 0:
            pass
        else:
            if kwargs:
                for key, value in kwargs.items():
                    if key == 'id':
                        self.id = value
                    elif key == 'size':
                        self.size = value
                    elif key == 'x':
                        self.x = value
                    elif key == 'y':
                        self.y = value
