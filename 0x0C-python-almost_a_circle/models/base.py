#!/usr/bin/python3
"""
This module contains the class: Base.
"""
import json


class Base:
    """
    This class is the base for all subsequent classes that will
    inherit from it.
    nb_objects is a private attribute that is used to give an id
    to an object that was created without one.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        This method instantiates the object.
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        This method returns a JSON string representation of
        a dictionary, 'list_dictionaries'.
        """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)
