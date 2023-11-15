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
        super().__init__(size, size, x, y, id)
        