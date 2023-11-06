#!/usr/bin/python3
"""
function that returns True if the object is
exactly an instance of the specified class ;
otherwise False.
Prototype: def is_same_class(obj, a_class):
"""


def is_same_class(obj, a_class):
    """
    function that returns True if the object is exactly an
    instance of the specified class ; otherwise False
    Args:
        obj(an instance of class)
        a_class(an instance of class)
    """
    if type(obj) == a_class:
        return True
    else:
        return False
