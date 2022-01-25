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
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Setter for Rectangle height.
        """
        self.__height = value

    @x.setter
    def x(self, value):
        """
        Setter for Rectangle x.
        """
        self.__x = value

    @y.setter
    def y(self, value):
        """
        Setter for Rectangle y.
        """
        self.__y = value
