#!/usr/bin/python3
"""
This module contain a function that read text file (UTF-8)
and prints it to stdout
Prototype: def read_file(filename=""):
"""


def read_file(filename=""):
    """
    Reads text file with UTF-8 encoding,
    Args:
        filename(filepath or directory)
    """
    with open(filename, encoding='utf-8') as a_file:
        for line in a_file:
            print(line.rstrip(), end='\n')
