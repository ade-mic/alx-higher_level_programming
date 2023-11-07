#!/usr/bin/python3
"""
module contain a class called BaseGeometry
Rectangle: inherits BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
     class Rectangle that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        object constructor
        """

        self.__width = width
        self.__height = height
        super().integer_validator('width', width)
        super().integer_validator('height', height)

    def __str__(self):
        return "[{}] {}/{}".format(__class__.__name__,
                                   self.__width, self.__height)

    def area(self):
        """ area of rectangle
        returns the area of the rectangle(width, height)
        """
        return self.__width * self.__height
