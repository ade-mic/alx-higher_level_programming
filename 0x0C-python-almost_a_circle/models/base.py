#!/usr/bin/python3
"""
This file contains a class name Base
"""


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
        import json
        filtered_list = [d
                         for d in list_dictionaries
                         if isinstance(d, dict)]
        if filtered_list is None:
            return '[]'
        elif len(filtered_list) == 0:
            return '[]'
        else:
            return json.dumps(filtered_list)
