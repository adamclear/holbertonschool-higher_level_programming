#!/usr/bin/python3
"""
This module contains the method: class_to_json.
"""


def class_to_json(obj):
    """
    This method returns the dictionary description of the
    JSON serialization of a class, 'obj'.
    """
    return obj.__dict__
