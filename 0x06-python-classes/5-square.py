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

    Methods:
        __init__(size): The constructor for Square class.
        area(): Returns the current square area
    """
    def __init__(self, size=0):
        """The constructor for Square class.

        Args:
            size (int): The length of the side of the square in units.

        Raises:
            TypeError: if not an integer
            ValueError: if <= 0
        """
        self.__size = size

    @property
    def size(self):
        """Int value of the size is return

        The setter validate the input type
        """
        return self.__size

    @size.setter
    def size(self, val):
        if type(val) is not int:
            raise TypeError('size must be an integer')
        elif val < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = val

    def area(self):
        """Return the square area
        Args:
            None
        """
        return self.__size ** 2

    def my_print(self):
        """ prints in stdout the square with the character #:
        if size is equal to 0, print an empty line
        Args:
            None
        """
        if self.size == 0:
            print('\n')
        else:
            for i in range(self.size):
                print("{}".format('#' * self.size))
