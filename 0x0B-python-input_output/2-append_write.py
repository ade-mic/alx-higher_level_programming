#!/usr/bin/python3
"""
This file contains a function that appends a string to a text file (UTF8)
and returns the number of characters written:
Prototype: def append_write(filename="", text="")::
"""


def append_write(filename="", text=""):
    """
    a function that writes a string to a text file (UTF8)
    and returns the number of characters written:
    Args:
        filename(directory or filepath)
        text (text to be written)
    """
    with open(filename, encoding='utf-8', mode='a') as a_file:
        n_char = a_file.write(text)
        return n_char
