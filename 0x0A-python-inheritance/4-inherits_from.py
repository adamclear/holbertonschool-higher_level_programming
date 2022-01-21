#!/usr/bin/python3
"""
This module contains the method: inherits_from.
"""


def inherits_from(obj, a_class):
    """
    This method checks if an object, 'obj', is an instance
    of a class that inherited (directly or indirectly) from
    the specified class, 'a_class'. Returns boolean True or
    False.
    """
    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
