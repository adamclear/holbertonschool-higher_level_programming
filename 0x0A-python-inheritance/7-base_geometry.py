#!/usr/bin/python3
"""
This module contains the class: BaseGeometry.
"""


class BaseGeometry:
    """
    This class does some awfully random things, currently.
    """
    def area(self):
        """
        This method raises an exception.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This method validates 'value' as an integer that is
        greater than 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 1:
            raise ValueError("{} must be greater than 0".format(name))
