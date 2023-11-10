#!/usr/bin/python3
"""
This file consist of a function that returns
the dictionary description with simple data structure
(list, dictionary, string, integer and boolean)
for JSON serialization of an object:
Prototype: def class_to_json(obj)
"""


def class_to_json(obj):
    """
    This function returns the dictionary discription
    with simple data structure for JSON serialization
    Args:
        Obj (serializable object)
    Returns:
        A dictionary
    """
    # check if the object id already a simple data structure
    if isinstance(obj, (list, dict, str, int, bool, float, type(None))):
        return obj
    # otherwise
    result = {}
    # iterate iver the object's attributes
    for attr in dir(obj):
        # if attribute is private or special attributes
        if attr.startswith('_'):
            continue
        # get the value of the attribute
        value = getattr(obj, attr)
        # check if the value is callable (method or function)
        if callable(value):
            continue
        # reconsively convert value to a simple data structure
        value = class_to_json(value)
        # add the attributes and value to the dictionary
        result[attr] = value
    # return dictionary
    return result
