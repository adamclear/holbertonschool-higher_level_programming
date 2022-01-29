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


class TestSquareClass(unittest.TestCase):
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
        Square1 = Square(10, 1, 2, 5)
        self.assertEqual(Square1.id, 5)
        self.assertEqual(Square1.size, 10)
        self.assertEqual(Square1.x, 1)
        self.assertEqual(Square1.y, 2)
        # Bad size
        with self.assertRaises(TypeError):
            Square2 = Square("ten", 1, 2, 5)
        with self.assertRaises(ValueError):
            Square2 = Square(-10, 1, 2, 5)
            Square2 = Square(0, 1, 2, 5)
        # Bad x
        with self.assertRaises(TypeError):
            Square2 = Square(10, "one", 2, 5)
        with self.assertRaises(ValueError):
            Square2 = Square(10, -1, 2, 5)
        # Bad y
        with self.assertRaises(TypeError):
            Square2 = Square(10, 1, "two", 5)
        with self.assertRaises(ValueError):
            Square2 = Square(10, 1, -2, 5)

    def test_size_setter(self):
        """
        Testing the setter for Square size.
        """
        Square1 = Square(10, 1, 2, 5)
        self.assertEqual(Square1.size, 10)
        Square1.size = 20
        self.assertEqual(Square1.size, 20)
        # Bad values/types
        with self.assertRaises(TypeError):
            Square1.size = "twenty"
        with self.assertRaises(ValueError):
            Square1.size = -20
            Square1.size = 0

if __name__ == "__main__":
    unittest.main()