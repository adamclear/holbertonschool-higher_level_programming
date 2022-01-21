#!/usr/bin/python3
"""
This module contains the method: class_to_json.
"""
import json


def class_to_json(obj):
    """
    This method returns the dictionary description of the
    JSON serialization of a class, 'obj'.
    """
    x = json.dumps(obj.__dict__)
    return json.loads(x)
