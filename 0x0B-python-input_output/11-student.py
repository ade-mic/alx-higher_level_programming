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
        from_json: replaces all attributes of the Student instance
    """
    def __init__(self, first_name, last_name, age):
        """
        Constructor of the class Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
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
        if isinstance(attrs, list):
            for item in attrs:
                if isinstance(item, str):
                    try:
                        value = getattr(self, item)
                        if callable(value):
                            continue
                        result[item] = value
                    except AttributeError:
                        pass
            # return result
            return result
        # otherwise attrs is not a list
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

    def reload_from_json(self, json):
        """
        replaces all attributes of the Student instance:
        A dictionary key will be the public attribute name
        A dictionary value will be the value of the public attribute
        Args:
            self (instance of Student)
            json (a dictionary)
        """
        for key, value in json.items():
            setattr(self, key, value)
