#!/usr/bin/python3
"""
 a function that returns True if the object is
 an instance of, or if the object is an instance of a class that 
 inherited- the specified class ; otherwise False.

Prototype: def is_kind_of_class(obj, a_class):
"""


def is_kind_of_class(obj, a_class):
    """
    returns True if the object is an instance of, 
    or if the object is an instance of a class that inherited - 
    the specified class ; otherwise False
    Args:
        obj (object)
        a_class (a class type)
    Returns:
        Boolean
    """
    if issubclass(type(obj), a_class):
        return True
    return False
