#!/usr/bin/python3
"""
This file contain  a function that load JSON file
and create an object
Prototype: def load_from_json_file(filename):
"""


def load_from_json_file(filename):
    """
    This fuction load JSON file and create an object
    Args:
        filename(path)
    """
    # import json
    import json
    # open filename for writing
    with open(filename) as a_file:
        obj_file = json.load(a_file)
    
