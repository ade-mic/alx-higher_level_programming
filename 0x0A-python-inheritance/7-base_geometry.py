#!/usr/bin/python3
"""
module contain a class called BaseGeometry
"""


class BaseGeometry:
    """
    Method:
        area(self)
        integer_validator(self, name, value)
    Attribute:
        None
    """

    def area(self):
        """
        Nothing implemeted yet
        Return:
            string: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        public instance that vavlidates value
        Args:
            name(str)
            value(int)
        Raise:
            TyperError if value is not integer
            ValueError is value < 0
        """
        if not isinstance(value, int):
            raise TypeError('{} must be ab integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
