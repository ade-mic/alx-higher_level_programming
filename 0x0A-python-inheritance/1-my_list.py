#!/usr/bin/python3
"""
 a class MyList that inherits from list:

Public instance method: def print_sorted(self): that prints the list, but sorted (ascending sort)
You can assume that all the elements of the list will be of type int
"""


class myList(list):
    """
    iherits from the list class or type
    Args: 
        list (list)
    Methods:
        prints_sorted: prints the list in ascending order
    """
def print_sorted(self, listItem):
    """
    prints the list in ascending order
    Args:
        self (list)
        listItem (list): integers to be printed in sorted array
    """
    item = listItem[:].sort()
