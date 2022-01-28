#!/usr/bin/python3
"""
Unittest for Base class.
"""
import unittest
import json
from models.base import Base
import pep8
import inspect


class TestBaseClass(unittest.TestCase):
    """
    The Base class test class.
    """
    @classmethod
    def setUpClass(cls) -> None:
        """
        Setup method.
        """
        cls.base_methods = inspect.getmembers(Base, inspect.isfunction)
    
    def test_pep8(self):
        """
        Testing pep8 compliance.
        """
        pep8_test = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """
        Testing module docstring.
        """
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Testing class docstring.
        """
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_method_docstring(self):
        """
        Testing method docstrings.
        """
        for methods, x in self.base_methods:
            self.assertTrue(len(methods[x].__doc__) >= 1)

if __name__ == "__main__":
    unittest.main()
