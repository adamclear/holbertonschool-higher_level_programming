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
    def test_pep8(self):
        """
        Testing pep8 compliance.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """
        Testing module docstring.
        """
        self.assertTrue(len('rectangle'.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Testing class docstring.
        """
        self.assertTrue(len(Rectangle.__doc__) >= 1)

    def test_method_docstring(self):
        """
        Testing method docstrings.
        """
        self.assertTrue(len(Rectangle.__init__.__doc__) >= 1)
        self.assertTrue(len(Rectangle.area.__doc__) >= 1)
        self.assertTrue(len(Rectangle.display.__doc__) >= 1)
        self.assertTrue(len(Rectangle.__str__.__doc__) >= 1)
        self.assertTrue(len(Rectangle.update.__doc__) >= 1)
        self.assertTrue(len(Rectangle.to_dictionary.__doc__) >= 1)

    def test_init(self):
        """
        Testing the init method.
        """
        Rectangle1 = Rectangle(10, 12, 1, 2, 5)
        self.assertEqual(Rectangle1.id, 5)
        self.assertEqual(Rectangle1.width, 10)
        self.assertEqual(Rectangle1.height, 12)
        self.assertEqual(Rectangle1.x, 1)
        self.assertEqual(Rectangle1.y, 2)
        # Bad args
        with self.assertRaises(TypeError):
            Rectangle2 = Rectangle(10, 10, 10, 10, 10, 10)
        with self.assertRaises(TypeError):
            Rectangle2 = Rectangle()
        # Bad width
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle2 = Rectangle(-10, 12, 1, 2, 5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle2 = Rectangle(0, 12, 1, 2, 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle2 = Rectangle("ten", 12, 1, 2, 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle2 = Rectangle(10.5, 12, 1, 2, 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle2 = Rectangle([], 12, 1, 2, 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle2 = Rectangle({}, 12, 1, 2, 5)
        # Bad height
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle2 = Rectangle(10, -12, 1, 2, 5)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle2 = Rectangle(10, 0, 1, 2, 5)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle2 = Rectangle(10, "twelve", 1, 2, 5)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle2 = Rectangle(10, 12.5, 1, 2, 5)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle2 = Rectangle(10, [], 1, 2, 5)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle2 = Rectangle(10, {}, 1, 2, 5)
        # Bad x
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle2 = Rectangle(10, 12, -1, 2, 5)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle2 = Rectangle(10, 12, "one", 2, 5)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle2 = Rectangle(10, 12, 1.5, 2, 5)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle2 = Rectangle(10, 12, [], 2, 5)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle2 = Rectangle(10, 12, {}, 2, 5)
        # Bad y
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle2 = Rectangle(10, 12, 1, -2, 5)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle2 = Rectangle(10, 12, 1, "two", 5)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle2 = Rectangle(10, 12, 1, 2.5, 5)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle2 = Rectangle(10, 12, 1, [], 5)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle2 = Rectangle(10, 12, 1, {}, 5)

    def test_width_setter(self):
        """
        Testing width setter.
        """
        Rectangle1 = Rectangle(10, 12, 1, 2, 5)
        Rectangle1.width = 20
        self.assertEqual(Rectangle1.width, 20)
        # Bad values/types
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle1.width = -20
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle1.width = 0
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle1.width = "twenty"
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle1.width = 20.5
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle1.width = []
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle1.width = {}

    def test_height_setter(self):
        """
        Testing height setter.
        """
        Rectangle1 = Rectangle(10, 12, 1, 2, 5)
        Rectangle1.height = 20
        self.assertEqual(Rectangle1.height, 20)
        # Bad values/types
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle1.height = -20
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle1.height = 0
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle1.height = "twenty"
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle1.height = 20.5
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle1.height = []
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle1.height = {}

    def test_x_setter(self):
        """
        Testing x setter.
        """
        Rectangle1 = Rectangle(10, 12, 1, 2, 5)
        Rectangle1.x = 20
        self.assertEqual(Rectangle1.x, 20)
        # Bad values/types
        with self.assertRaises(ValueError):
            Rectangle1.x = -20
        with self.assertRaises(TypeError):
            Rectangle1.x = "twenty"

    def test_y_setter(self):
        """
        Testing y setter.
        """
        Rectangle1 = Rectangle(10, 12, 1, 2, 5)
        Rectangle1.y = 20
        self.assertEqual(Rectangle1.y, 20)
        # Bad values/types
        with self.assertRaises(ValueError):
            Rectangle1.y = -20
        with self.assertRaises(TypeError):
            Rectangle1.y = "twenty"

    def test_area(self):
        """
        Testing area method.
        """
        Rectangle1 = Rectangle(10, 12, 1, 2, 5)
        rect_area = Rectangle1.area()
        self.assertTrue(type(rect_area) is int)
        self.assertEqual(rect_area, 120)

    def test_update(self):
        """
        Testing the update method.
        """
        Rectangle1 = Rectangle(10, 10, 1, 2, 5)
        # Using args
        Rectangle1.update(10, 20, 20, 2, 3)
        self.assertEqual(Rectangle1.id, 10)
        self.assertEqual(Rectangle1.width, 20)
        self.assertEqual(Rectangle1.height, 20)
        self.assertEqual(Rectangle1.x, 2)
        self.assertEqual(Rectangle1.y, 3)
        # Using kwargs
        Rectangle1.update(height=30, width=30, id=20, x=3, y=4)
        self.assertEqual(Rectangle1.width, 30)
        self.assertEqual(Rectangle1.height, 30)
        self.assertEqual(Rectangle1.id, 20)
        self.assertEqual(Rectangle1.x, 3)
        self.assertEqual(Rectangle1.y, 4)

    def test_to_dictionary(self):
        """
        Testing the to_dictionary method.
        """
        Rectangle1 = Rectangle(10, 10, 1, 2, 5)
        Rectangle1_dict = Rectangle1.to_dictionary()
        self.assertTrue(type(Rectangle1_dict) is dict)
        dict1 = {'id': 5, 'width': 10, 'height': 10, 'x': 1, 'y': 2}
        self.assertEqual(Rectangle1_dict, dict1)

if __name__ == "__main__":
    unittest.main()