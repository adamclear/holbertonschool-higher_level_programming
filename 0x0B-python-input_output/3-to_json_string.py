#!/usr/bin/python3
"""
This module contains the method: to_json_string.
"""
import json


def to_json_string(my_obj):
    """
    This method returns the JSON representation of an
    object, 'my_obj'.
    """
    return json.dumps(my_obj)
