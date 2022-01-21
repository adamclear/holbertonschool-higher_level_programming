#!/usr/bin/python3
"""
This module contains the method: is_same_class.
"""


def is_same_class(obj, a_class):
    """
    This method checks to see if an object, 'obj', is an
    instance of a particular class, 'a_class'. Returns boolean
    True or False.
    """
    return (type(obj) == a_class)
