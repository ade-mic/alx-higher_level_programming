#!/usr/bin/python3
"""
This module defines the Square class.

The Square class is used to represent and manipulate squares.
"""


class Square:
    """
    An empty class Square that defines a square
    the class is empty.

    Attributes:
        size(int):  an int type that must >= 0 to represent size of square
    """
    def __init__(self, size=0):
        """The constructor for Square class.

        Args:
            size (int): The length of the side of the square in units.
        """
        self.__size = size
