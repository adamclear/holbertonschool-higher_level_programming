#!/usr/bin/python3
"""
This module contains the class: Square.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    This class creates an object, square, that is of a particular
    size, 'size'.
    """
    def __init__(self, size):
        """
        This method creates the object.
        """
        self.integer_validator("size", size)
        self.__size = size
        self.__width = size
        self.__height = size

    def area(self):
        """
        This method returns the area of the object.
        """
        return self.__size * self.__size

    def __str__(self):
        """
        This method provides the string width and height
        of the object.
        """
        return "[Square] {:d}/{:d}".format(self.__width, self.__height)
