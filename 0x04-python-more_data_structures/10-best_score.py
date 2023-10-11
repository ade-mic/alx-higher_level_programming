#!/usr/bin/python3
def best_score(a_dictionary):
    """
    Write a function that returns a key
    with the biggest integer value.
    """
    if a_dictionary is not None:
        res = 0
        for key, value in a_dictionary.items():
            if a_dictionary[key] > res:
                res = a_dictionary[key]
        return res
    else:
        return None
