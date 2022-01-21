#!/usr/bin/python3
"""
This module contains the method: write_file.
"""


def write_file(filename="", text=""):
    """
    The method writes a string, 'text', to a file, 'filename'.
    If the file does not exist, it will create the file.
    If the file is not empty, it will overwrite the contents.
    """
    length = len(text)
    with open(filename, "w") as x:
        x.write(text)
    return length
