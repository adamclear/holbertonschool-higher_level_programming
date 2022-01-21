#!/usr/bin/python3
"""
This module contains the method: read_file.
"""


def read_file(filename=""):
    """
    This method reads a file, 'filename', and prints the
    contents to stdout.
    """
    with open(filename) as x:
        for line in x:
            print(line, end="")
