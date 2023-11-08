#!/usr/bin/python3
"""
This file contain a function that returns
the JSON representation of an object(string)
"""


def to_json_string(obj):
    """
    This fuction returns the JSON representation
    of an object (string)
    Args:
        obj(string)
    """
    import json
    return json.dumps(obj)
