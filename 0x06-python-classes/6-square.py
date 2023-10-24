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
    def __init__(self, size=0, position=(0, 0)):
        """The constructor for Square class.

        Args:
            size (int): The length of the side of the square in units.

        Raises:
            TypeError: if not an integer
            ValueError: if <= 0
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """
        To retrieve the value of position
        position must be a tuple of 2 positive integers,
        Raises:
            a TypeError exception
            with the message position must be a tuple of 2 positive integers
        """
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def area(self):
        """Return the square area
            Args:
                None
        """
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character #:
        if size is equal to 0, print an empty line
        Args:
            None
        """
        if self.__size == 0:
            print('')
        else:
            for i in range(self.__size):
                if self.__position[1] > 0:
                    print("{}".format('#' * self.__size))
                else:
                    print("{}{}".
                        format(' ' * self.__position[0], '#' * self.__size))
