#!/usr/bin/python3
"""
This module contains the method: is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
    This method checks if an object, 'obj', is an instance of,
    or an instance of a class that inherited from, 'a_class'.
    Returns boolean True or False.
    """
    return isinstance(obj, (a_class))
