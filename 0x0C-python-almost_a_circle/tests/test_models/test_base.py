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


class TestBaseClass(unittest.TestCase):
    """
    The Base class test class.
    """
    def tearDown(self):
        """
        Teardown method.
        """
        Base.clear()

    def test_1_pep8(self):
        """
        Testing pep8 compliance.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_2_module_docstring(self):
        """
        Testing module docstring.
        """
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_3_class_docstring(self):
        """
        Testing class docstring.
        """
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_4_method_docstring(self):
        """
        Testing method docstrings.
        """
        self.assertTrue(len(Base.__init__.__doc__) >= 1)
        self.assertTrue(len(Base.to_json_string.__doc__) >= 1)
        self.assertTrue(len(Base.save_to_file.__doc__) >= 1)
        self.assertTrue(len(Base.from_json_string.__doc__) >= 1)
        self.assertTrue(len(Base.create.__doc__) >= 1)
        self.assertTrue(len(Base.load_from_file.__doc__) >= 1)

    def test_5_init(self):
        """
        Tests the init method.
        """
        base1 = Base(10)
        self.assertEqual(base1.id, 10)
        base2 = Base(100)
        self.assertEqual(base2.id, 100)
        base3 = Base()
        self.assertEqual(base3.id, 1)

    def test_6_to_json_string(self):
        """
        Tests the to_json_string method.
        """
        dict1 = {'id': 50}
        dict2 = {'id': 100}
        json_string = Base.to_json_string([dict1])
        self.assertTrue(type(json_string) is str)
        json_string = Base.to_json_string([dict1, dict2])
        self.assertTrue(type(json_string) is str)
        json_dict = json.loads(json_string)
        self.assertEqual(json_dict, [dict1, dict2])
        # Arg is empty list
        json_string2 = Base.to_json_string([])
        self.assertTrue(type(json_string2) is str)
        self.assertEqual(json_string2, "[]")
        # No arg
        with self.assertRaises(TypeError):
            json_string2 = Base.to_json_string()

    def test_7_save_to_file(self):
        """
        Tests the save_to_file method.
        """
        Rectangle1 = Rectangle(10, 12, 1, 2, 5)
        Rectangle2 = Rectangle(20, 20, 2, 3, 10)
        Rectangle.save_to_file([Rectangle1])
        with open("Rectangle.json", "r") as file:
            self.assertTrue(len(file.read()) == 54)
        # No arg
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()
        # Too many args
        with self.assertRaises(TypeError):
            Rectangle.save_to_file([Rectangle1], [Rectangle2])
        # Setup for load_from_file test
        Rectangle.save_to_file([Rectangle1])

    def test_8_from_json_string(self):
        """
        Testing the from_json_string method.
        """
        json_string1 = '[{"id": 5, "width": 10, "height": 12, "x": 1, "y": 2}]'
        json_list1 = Base.from_json_string(json_string1)
        self.assertTrue(type(json_list1) is list)
        # Empty string
        json_string2 = ""
        json_list2 = Base.from_json_string(json_string2)
        self.assertTrue(type(json_list2) is list)
        # No arg
        with self.assertRaises(TypeError):
            json_list3 = Base.from_json_string()
        # Too many args
        with self.assertRaises(TypeError):
            json_list3 = Base.from_json_string(json_string1, json_string2)

    def test_9_create(self):
        """
        Testing the create method.
        """
        square_dict1 = {'id': 5, 'size': 10, 'x': 1, 'y': 2}
        square_dict2 = {}
        Square_create1 = Square.create(**square_dict1)
        self.assertTrue(type(Square_create1) is Square)
        # No arg
        Square_create2 = Square.create()
        self.assertTrue(type(Square_create2) is Square)
        # Too many args
        with self.assertRaises(TypeError):
            Square_create2 = Square.create(square_dict1, square_dict2)

    def test_a1_load_from_file(self):
        """
        Testing the load_from_file method.
        """
        Rectangle_list = Rectangle.load_from_file()
        self.assertTrue(type(Rectangle_list) is list)
        self.assertTrue(len(Rectangle_list) == 1)
        # No file
        Square_list = Square.load_from_file()
        self.assertTrue(type(Square_list) is list)
        self.assertTrue(len(Square_list) == 0)
        # Passing an arg
        with self.assertRaises(TypeError):
            Oops_list = Rectangle.load_from_file(Rectangle)

if __name__ == "__main__":
    unittest.main()
