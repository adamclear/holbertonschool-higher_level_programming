#!/usr/bin/python3
"""
This module contains the class: MyList.
MyList inherits from superclass: list.
"""


class MyList(list):
    """
    This class is a subclass of list.
    """
    def __init__(self):
        """
        This method initializes the class.
        """
        pass

    def print_sorted(self):
        """
        This method prints the list contained in self.
        The data is printed in sorted (ascending) order.
        """
        print(sorted(self))
