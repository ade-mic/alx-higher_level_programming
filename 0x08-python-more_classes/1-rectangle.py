#!/usr/bin/python3
""" 0-reactangle consist of
class rectangle
"""


class Rectangle:
    """Rectangle create a
    rectangular shape with width and height
    """
    def __init__(self, width=0, height=0):
        """__init__ initialize the class with a
        width and height
        Args:
            width(int)
            height(int)
        """
        self.__width = width
        self.__height = height
    @property
    def width(self):
        """
        Returns the value of width
        """
        return self.__width
    @width.setter
    def width(self, value):
        """
        Set the value of width
        Args:
            value(int): integer value
        Raises:
             TypeError if not int
             ValueError if less than 0
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise TypeError('width must be >= 0')
        self.__width = value


    @property
    def height(self):
        """
        To retrieve height
        """
        return self.__height
    @height.setter
    def height(self, value):
        """
        To set the value of height
        Args:
            value (int): must be an integer
        Raises:
            TypeError: if value is not type int
            ValueError: if value < 0
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
