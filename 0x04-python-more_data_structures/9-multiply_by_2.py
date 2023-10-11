#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """
    Write a function that returns a new dictionary with all values multiplied by 2
    """
    res = {}
    for x, y in a_dictionary.items():
        res[x] = y * 2
    return res
