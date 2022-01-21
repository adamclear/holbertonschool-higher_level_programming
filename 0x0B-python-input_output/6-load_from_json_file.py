#!/usr/bin/python3
"""
This module contains the method: load_from_json_file.py
"""
import json


def load_from_json_file(filename):
    """
    This method creates an object from a JSON file, 'filename'.
    """
    with open(filename) as x:
        return json.load(x)
