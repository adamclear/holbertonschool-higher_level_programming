#!/usr/bin/python3
"""
This module contains the method: save_to_json_file.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    This method writes a JSON representation of an
    object, 'my_obj', to a file, 'filename'.
    If the file does not exist, it will be created.
    """
    with open(filename, "w") as x:
        x.write(json.dumps(my_obj))
