#!/usr/bin/python3
"""
This file contains a class name Base
"""
import json


class Base:
    """
    private class attribute __nb_objects = 0
    Method:
        class constructor: def __init__(self, id=None)::
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Args:
            self(instance of Base)
            id (integer)
        """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Args:
            list_dictionaries (list of dictionaries)
        Returns
            JSON string representation of list_dictionarie
            If list_dictionaries is None or empty, return the string: "[]"
        """
        if list_dictionaries is None:
            return '[]'
        elif len(list_dictionaries) == 0:
            return '[]'
        else:
            filtered_list = [d
                             for d in list_dictionaries
                             if isinstance(d, dict)]
            return json.dumps(filtered_list)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file:
        """
        filename = cls.__name__ + '.json'
        with open(filename, mode='w') as file:
            if list_objs is None:
                file.write('[]')
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation
        """
        if json_string is None or json_string == '[]':
            return []
        else:
            return json.loads(json_string)
