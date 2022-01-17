#!/usr/bin/python3
"""
This module contains the class: Rectangle.
"""


class Rectangle:
    """
    This class defines a Rectangle object based on width & height.
    """
    def __init__(self, width=0, height=0):
        """
        This method initializes the object.
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """
        Getter for rectangle width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for rectangle width.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for rectangle height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for rectangle height.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
