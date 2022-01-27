#!/usr/bin/python3
"""
This module contains the subclass: Square.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This class inherits from superclass, Rectangle. An object of
    this class is defined by attributes; size, x, and y.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        This method instantiates the object. All attributes
        are instantiated using the init from the superclass.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        This method returns a string representation of the
        Square object.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)
