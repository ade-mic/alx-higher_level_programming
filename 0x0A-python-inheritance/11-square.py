#!/usr/bin/python3
"""
module contain a class called BaseGeometry
Rectangle: inherits BaseGeometry
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
     class Square that inherits Rectangle
    """
    def __init__(self, size):
        """
        object constructor
        """
        super().__init__(size, size)
        self.__size = size
        super().integer_validator('size', size)

    def __str__(self):
        return "[{}] {}/{}".format(__class__.__name__, self.__size, self.__size)

    def area(self):
        """ area of rectangle
        returns the area of the rectangle(width, height)
        """
        return self.__size ** 2
