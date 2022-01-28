#!/usr/bin/python3
"""
Unittest for Base class.
"""
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import pep8
import inspect


class TestBaseClass(unittest.TestCase):
    """
    The Base class test class.
    """
    @classmethod
    def setUpClass(cls):
        """
        Setup method.
        """
        cls.base_methods = inspect.getmembers(Base, inspect.isfunction)
    
    def test_pep8(self):
        """
        Testing pep8 compliance.
        """
        pep8style = pep8.StyleGuide(quiet=True)
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
            self.assertTrue(len(methods.__doc__) >= 1)

    def test_init(self):
        """
        Tests the init method.
        """
        base1 = Base()
        self.assertEqual(base1.id, 1)
        base2 = Base(100)
        self.assertEqual(base2.id, 100)
        base3 = Base()
        self.assertEqual(base3.id, 2)

    def test_to_json_string(self):
        """
        Tests the to_json_string method.
        """
        dict1 = {'width': 2, 'height': 2, 'x': 1, 'y': 1, 'id': 50}
        dict2 = {'width': 3, 'height': 3, 'x': 2, 'y': 2, 'id': 100}
        json_string = Base.to_json_string([dict1, dict2])
        self.assertTrue(type(json_string) is str)
        json_dict = json.loads(json_string)
        self.assertEqual(json_dict, [dict1, dict2])

if __name__ == "__main__":
    unittest.main()
