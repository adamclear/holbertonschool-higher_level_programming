#!/usr/bin/python3
"""
Unittest for Rectangle class.
"""
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import pep8
import inspect


class TestRectangleClass(unittest.TestCase):
    """
    The Rectangle class test class.
    """
    @classmethod
    def setUpClass(cls):
        """
        Setup method.
        """
        cls.base_methods = inspect.getmembers(Square, inspect.isfunction)

    def test_pep8(self):
        """
        Testing pep8 compliance.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """
        Testing module docstring.
        """
        self.assertTrue(len(Square.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Testing class docstring.
        """
        self.assertTrue(len(Square.__doc__) >= 1)

    def test_method_docstring(self):
        """
        Testing method docstrings.
        """
        for methods in self.base_methods:
            self.assertTrue(len(methods.__doc__) >= 1)

    def test_init(self):
        """
        Testing the init method.
        """
        Square1 = Square(10, 12, 1, 2, 5)
        self.assertEqual(Square1.id, 5)
        self.assertEqual(Square1.width, 10)
        self.assertEqual(Square1.height, 12)
        self.assertEqual(Square1.x, 1)
        self.assertEqual(Square1.y, 2)

if __name__ == "__main__":
    unittest.main()