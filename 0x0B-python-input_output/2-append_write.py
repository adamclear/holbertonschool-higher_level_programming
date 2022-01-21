#!/usr/bin/python3
"""
This module contains the method: append_write.
"""


def append_write(filename="", text=""):
    """
    This method appends a string, 'text', to a file, 'filename'.
    If the file doesn't exist, it will be created.
    """
    length = len(text)
    with open(filename, "a") as x:
        x.write(text)
    return length
