#!/usr/bin/python3
"""
This module contains the class: Base.
"""


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
