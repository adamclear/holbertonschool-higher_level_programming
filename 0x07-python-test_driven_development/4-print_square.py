#!/usr/bin/python3
"""
This module contains the function print_square.
python3 -c 'print(__import__("4-print_square").__doc__)'
"""


def print_square(size):
    """
    This function prints a square to stdout based on 'size'.
    'size' must be an integer or float equal to or greater
    than 0.
    python3 -c 'print(__import__("4-print_square").print_square.__doc__)'
    """
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print()
    for x in range(size):
        for y in range(size):
            print("#", end="")
        print()
