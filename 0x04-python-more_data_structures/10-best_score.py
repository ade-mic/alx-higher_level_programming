#!/usr/bin/python3
def best_score(a_dictionary):
    """
    Write a function that returns a key
    with the biggest integer value.
    """
    if a_dictionary is not None:
        return max(a_dictionary)
    else:
        return None
