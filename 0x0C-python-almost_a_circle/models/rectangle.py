#!/usr/bin/python3
"""
This file contains a class name Rectangle
"""

from models.base import Base


class Rectangle (Base):
    """
    Class inherits from Base
    Method:
        class constructor: def __init__(
            self, width, height, x=0, y=0, id=None
            ):
    """
    __nb_objects = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Args:
            self(instance of Base)
            id (integer)
        """
        super().__init__(id=id)
        # check if width is an int
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        # check if width is greater than 0
        if width <= 0:
            raise ValueError('width must be > 0')
        # check if height is integer
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        # check if height is greater than 0
        if height <= 0:
            raise ValueError('height must be > 0')
        # check if x is an integer
        if not isinstance(x, int):
            raise TypeError('x must be an integer')
        # check if x < 0
        if x < 0:
            raise ValueError('x must be >= 0')
        # check if y is an integer
        if not isinstance(y, int):
            raise TypeError('y must be an integer')
        # check if y is less than 0
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        returns the value of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        set the attribute value of width
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """
        returns the value of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        set the attribute value of height
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """
        returns the value of x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        set the attribute value of x
        """
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')

        self.__x = value

    @property
    def y(self):
        """
        returns the value of y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        set the attribute value of y
        """
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """
        returns the area value of the Rectangle instance
        Args:
            self(Rectangle instance)
        """
        return self.__height * self.__width

    def display(self):
        """
        prints out to the stdout the Rectangle instance with
        character #
        Args:
            self(instance of Rectangle)
        """
        print_y = True
        for i in range(self.__height):
            if print_y:
                print('\n' * self.__y, end='')
                print_y = False
            print('{}{}'.format(' '*self.__x,  '#' * self.__width))

    def __str__(self):
        """
        Returns the string representation of Rectangle class
        """
        return '[{}] ({}) {}/{} - {}/{}'.format(type(self).__name__,
                                                self.id, self.__x, self.__y,
                                                self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
        Public method assigns an position arguement to each attrubute
        Args:
            1st argument should be the id attribute
            2nd argument should be the width attribute
            3rd argument should be the height attribute
            4th argument should be the x attribute
            5th argument should be the y attribute
         """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'width':
                    self.__width = value
                elif key == 'height':
                    self.__height = value
                elif key == 'x':
                    self.__x = value
                elif key == 'y':
                    self.__y = value
                elif key == 'id':
                    self.id = value
        if args:
            if len(args) == 1:
                self.id = args[0]
            elif len(args) == 2:
                self.id = args[0]
                self.__width = args[1]
            elif len(args) == 3:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
            elif len(args) == 4:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
            else:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]

    def to_dictionary(self):
        """
        Returns the dictionary representation of a
        Rectangle instance
        """
        return {'id': self.id,
                'width': self.__width,
                'height': self.__height,
                'x': self.__x,
                'y': self.__y}
