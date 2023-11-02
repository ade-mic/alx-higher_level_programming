#!/usr/bin/python3
"""
function that prints a text with
2 new lines after each of these characters: ., ? and :
Prototype: def text_indentation(text):
"""


def text_indentation(text):
    """def text_indentation
        Args(str)
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    line = text.split(".")
    new_text = ".\n\n".join(line)
    line = new_text.split("?")
    new_text = "?\n\n".join(line)
    line = new_text.split(":")
    new_text = ":\n\n".join(line)
    print(new_text)
