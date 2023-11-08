#!/usr/bin/python3
"""
This file contain a function
that returns an object (Python data structure)
represented by a JSON string
"""


def from_json_string(my_str):
    """
    This fuction returns the python object representation
    of an json string
    Args:
        my_str(string)
    """
    import json
    return json.loads(my_str)
