#!/usr/bin/python3
"""
This file contain a class Student that defines a student by:
Public instance attributes:
first_name
last_name
age
"""


class Student:
    """
    Public Attributes:
        first_name
        last_name
        age
    Method:
        __init__: Construct an instance of student
        to_json: retrieves a dictionaey representation od a Student instance
    """
    def __init__(self, first_name, last_name, age):
        """
        Constructor of the class Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        This method returns the dictionary discription
        with simple data structure for JSON serialization
        Args:
            self (serializable object)
        Returns:
            A dictionary
        """
        # check if the object id already a simple data structure
        # if isinstance(self, (list, dict, str, int, bool, float, type(None))):
        #     return self
        # # otherwise
        result = {}
        # # iterate iver the object's attributes
        for attr in dir(self):
            # if attribute is private or special attributes
            if attr.startswith('_') and attr.endswith('_'):
                continue
            # get the value of the attribute
            value = getattr(self, attr)
            # check if the value is callable (method or function)
            if callable(value):
                continue
            # add the attributes and value to the dictionary
            result[attr] = value
        # return dictionary
        return result
