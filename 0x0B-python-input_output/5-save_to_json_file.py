#!/usr/bin/python3
"""
This file contain  a function that writes an
Object to a text file, using a JSON representation:
Prototype: def save_to_json_file(my_obj, filename):
"""


def save_to_json_file(my_obj, filename):
    """
    This fuction writea an object to a text file
    using a JSON representation
    Args:
        my_obj (string)
        filename(path)
    """
    # import json
    import json
    # open filename for writing
    with open(filename, "w") as a_file:
        json.dump(my_obj, a_file)
