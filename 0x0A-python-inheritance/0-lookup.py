#!/usr/bin/python3
"""
A function that returns the list
of available and methods of an object
Prototype: def lookup(obj)
"""


def lookup(obj):
    """returns the list of available
    attributes and methods
    Args:
        obj (object)
    """
    return dir(obj)


