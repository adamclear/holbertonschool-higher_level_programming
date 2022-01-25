#!/usr/bin/python3
"""
This module contains the subclass: Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    This class inherits from superclass, Base. An object of this
    class is defined by private attributes; width, height, x,
    and y.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        This method instantiates the object. The id is
        instantiated using the init from the superclass.
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        Getter for Rectangle width.
        """
        return self.__width
    
    @property
    def height(self):
        """
        Getter for Rectangle height.
        """
        return self.__height

    @property
    def x(self):
        """
        Getter for Rectangle x.
        """
        return self.__x

    @property
    def y(self):
        """
        Getter for Rectangle y.
        """
        return self.__y
    
    @width.setter
    def width(self, value):
        """
        Setter for Rectangle width.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Setter for Rectangle height.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """
        Setter for Rectangle x.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """
        Setter for Rectangle y.
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
