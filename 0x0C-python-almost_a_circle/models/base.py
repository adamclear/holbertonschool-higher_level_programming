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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        This method writes the JSON string representation of an
        object, 'list_objs', to a file.
        """
        filename = cls.__name__ + ".json"
        newstring = []
        if list_objs:
            for item in list_objs:
                newstring.append(cls.to_dictionary(item))
        with open(filename, "w") as file:
            file.write(cls.to_json_string(newstring))

    @staticmethod
    def from_json_string(json_string):
        """
        This method returns the list of the JSON string, 'json_string'.
        """
        if not json_string:
            return []
        return json.loads(json_string)
