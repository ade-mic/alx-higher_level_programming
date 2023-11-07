#!/usr/bin/python3
"""
a function that returns True if the object is an instance of a class
that inherited (directly or indirectly) fromm the specified class ;
otherwise False
"""


def inherits_from(obj, a_class):
    """
    a function returns True id the obj is an instance of a_class
    and False otherwise
    Args:
        obj(class)
        a_class(class)
    Returns:
        Boolean
    """
    obj_type = type(obj)
    for base_class in obj_type.__bases__:
        if issubclass(base_class, a_class):
            return True
    return False
