#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    Write a function that deletes a key in a dictionary.
    """
    if a_dictionary.get(key):
        a_dictionary.pop(key)
    return a_dictionary
