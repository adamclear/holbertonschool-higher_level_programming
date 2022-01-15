#!/usr/bin/python3
"""
Module 0-add_integer
This module contains the function add_integer.
python3 -c 'print(__import__("my_module").__doc__)'
"""


def add_integer(a, b=98):
    """
    This function adds two integers together and returns the
    result. It can accept either integers or floats as
    arguments. However, if a float is passed as an argument
    it will be cast to an integer.
    python3 -c 'print(__import__("my_module").my_function.__doc__)'
    """
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")
    return a + b
