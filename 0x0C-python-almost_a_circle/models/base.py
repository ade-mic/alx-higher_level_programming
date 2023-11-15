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

    def to_json_string(list_dictionaries):
        import json
        """
        Args:
            list_dictionaries (list of dictionaries)
        Returns
            JSON string representation of list_dictionarie
            If list_dictionaries is None or empty, return the string: "[]"
        """
        if len(list_dictionaries) == 0 or list_dictionaries is None:
            return '[]'
        else:
            return json.dumps(list_dictionaries)
