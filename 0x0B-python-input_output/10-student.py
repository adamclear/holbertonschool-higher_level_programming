#!/usr/bin/python3
"""
This module contains the class: Student.
"""


class Student:
    """
    This class creates a Student object that has; a first_name,
    last_name, and age.
    """
    def __init__(self, first_name, last_name, age):
        """
        This method initializes the object.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        This method returns a dictionary representation of
        itself.
        """
        if attrs is None or type(attrs) is not list:
            return self.__dict__
        new_dict = {}
        cur_dict = self.__dict__
        for key, value in cur_dict.items():
            if key in attrs:
                new_dict[key] = value
        return new_dict
