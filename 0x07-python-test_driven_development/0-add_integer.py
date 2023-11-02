#!usr/bin/python3
""" Add intergers
Prototype: def add_integer(a, b=98):
a and b must be integers or floats, otherwise raise a TypeError exception with
the message a must be an integer or b must be an integer 
"""


def add_integer(a, b=98):
    """ add_integers
    Args:
        a(int): first paramter
        b(int): second parameter

    Returns:
        int: the sum of a and b
    Raises:
        Typerror: if a or b not int or float
    """
    if not isinstance(a, int):
        if isinstance(a, float):
            a = int(a)
        else:
            raise TypeError("a must be an integer")
    if not isinstance(b, int):
        if isinstance(b, float):
            b = int(b)
        else:
            raise TypeError("b must be an integer")
    return a + b
