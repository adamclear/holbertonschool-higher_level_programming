#!/usr/bin/python3
"""
This module contains the class: Rectangle.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    This class is a subclass of BaseGeometry. It creates a
    rectangle object of a specific (width, height) size. If width
    or height are not integers, or are less than 1, then it will
    not create the object.
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        This method returns the area of the object.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        This method provides the string width and height of
        the object.
        """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
