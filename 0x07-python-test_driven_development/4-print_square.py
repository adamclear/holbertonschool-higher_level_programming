#!/usr/bin/python3
"""
This module contains the function print_square.
"""


def print_square(size):
    """
    This function prints a square to stdout based on 'size'.
    'size' must be an integer or float equal to or greater
    than 0.
    """
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for x in range(size):
        for y in range(size):
            print("#", end="")
        print()
