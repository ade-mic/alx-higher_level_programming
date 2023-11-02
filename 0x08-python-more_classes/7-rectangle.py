#!/usr/bin/python3
""" 0-reactangle consist of
class rectangle
"""


class Rectangle:
    """Rectangle create a
    rectangular shape with width and height
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0, print_symbol='#'):
        """__init__ initialize the class with a
        width and height
        Args:
            width(int)
            height(int)
        """
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

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
            raise ValueError('width must be >= 0')
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

    def area(self):
        """ Returns the area of rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """ Retuurn the perimeter of a rectangle instance"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """String representation of rectangle using #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return (
            ((str(self.print_symbol) * self.__width + "\n")
             * (self.__height - 1)
                + str(self.print_symbol) * self.__width)
            )

    def __repr__(self):
        """ return string representation of
        rectangle class that can be parse to an object"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Delete an instance of Rectangle"""
        print('Bye rectangle...')
        type(self).number_of_instances -= 1
