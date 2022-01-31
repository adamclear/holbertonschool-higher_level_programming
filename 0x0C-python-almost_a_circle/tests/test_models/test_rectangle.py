#!/usr/bin/python3
"""
Unittest for Rectangle class.
"""
import unittest
from models.rectangle import Rectangle
import pep8


class TestRectangleClass(unittest.TestCase):
    """
    The Rectangle class test class.
    """
    def tearDown(self):
        """
        Teardown method.
        """
        Rectangle.clear()

    def test_1_pep8(self):
        """
        Testing pep8 compliance.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_2_module_docstring(self):
        """
        Testing module docstring.
        """
        self.assertTrue(len(Rectangle.__doc__) >= 1)

    def test_3_class_docstring(self):
        """
        Testing class docstring.
        """
        self.assertTrue(len(Rectangle.__doc__) >= 1)

    def test_4_method_docstring(self):
        """
        Testing method docstrings.
        """
        self.assertTrue(len(Rectangle.__init__.__doc__) >= 1)
        self.assertTrue(len(Rectangle.width.__doc__) >= 1)
        self.assertTrue(len(Rectangle.height.__doc__) >= 1)
        self.assertTrue(len(Rectangle.x.__doc__) >= 1)
        self.assertTrue(len(Rectangle.y.__doc__) >= 1)
        self.assertTrue(len(Rectangle.area.__doc__) >= 1)
        self.assertTrue(len(Rectangle.display.__doc__) >= 1)
        self.assertTrue(len(Rectangle.__str__.__doc__) >= 1)
        self.assertTrue(len(Rectangle.update.__doc__) >= 1)
        self.assertTrue(len(Rectangle.to_dictionary.__doc__) >= 1)

    def test_5_init(self):
        """
        Testing the init method.
        """
        Rectangle1 = Rectangle(10, 12, 1, 2, 5)
        self.assertEqual(Rectangle1.id, 5)
        self.assertEqual(Rectangle1.width, 10)
        self.assertEqual(Rectangle1.height, 12)
        self.assertEqual(Rectangle1.x, 1)
        self.assertEqual(Rectangle1.y, 2)
        Rectangle2 = Rectangle(1, 2)
        self.assertEqual(Rectangle2.id, 1)
        self.assertEqual(Rectangle2.width, 1)
        self.assertEqual(Rectangle2.height, 2)
        self.assertEqual(Rectangle2.x, 0)
        self.assertEqual(Rectangle2.y, 0)
        Rectangle3 = Rectangle(1, 2, 3)
        self.assertEqual(Rectangle3.id, 2)
        self.assertEqual(Rectangle3.width, 1)
        self.assertEqual(Rectangle3.height, 2)
        self.assertEqual(Rectangle3.x, 3)
        self.assertEqual(Rectangle3.y, 0)
        Rectangle4 = Rectangle(1, 2, 3, 4)
        self.assertEqual(Rectangle4.id, 3)
        self.assertEqual(Rectangle4.width, 1)
        self.assertEqual(Rectangle4.height, 2)
        self.assertEqual(Rectangle4.x, 3)
        self.assertEqual(Rectangle4.y, 4)
        # Bad args
        with self.assertRaises(TypeError):
            Rectangle5 = Rectangle(10, 10, 10, 10, 10, 10)
        with self.assertRaises(TypeError):
            Rectangle5 = Rectangle()
        # Bad width
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle5 = Rectangle(-10, 12, 1, 2, 5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle5 = Rectangle(0, 12, 1, 2, 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle5 = Rectangle("ten", 12, 1, 2, 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle5 = Rectangle(10.5, 12, 1, 2, 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle5 = Rectangle([], 12, 1, 2, 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle5 = Rectangle({}, 12, 1, 2, 5)
        # Bad height
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle5 = Rectangle(10, -12, 1, 2, 5)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle5 = Rectangle(10, 0, 1, 2, 5)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle5 = Rectangle(10, "twelve", 1, 2, 5)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle5 = Rectangle(10, 12.5, 1, 2, 5)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle5 = Rectangle(10, [], 1, 2, 5)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle5 = Rectangle(10, {}, 1, 2, 5)
        # Bad x
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle5 = Rectangle(10, 12, -1, 2, 5)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle5 = Rectangle(10, 12, "one", 2, 5)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle5 = Rectangle(10, 12, 1.5, 2, 5)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle5 = Rectangle(10, 12, [], 2, 5)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle5 = Rectangle(10, 12, {}, 2, 5)
        # Bad y
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle5 = Rectangle(10, 12, 1, -2, 5)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle5 = Rectangle(10, 12, 1, "two", 5)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle5 = Rectangle(10, 12, 1, 2.5, 5)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle5 = Rectangle(10, 12, 1, [], 5)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle5 = Rectangle(10, 12, 1, {}, 5)

    def test_6_width_setter(self):
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

    def test_7_height_setter(self):
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

    def test_8_x_setter(self):
        """
        Testing x setter.
        """
        Rectangle1 = Rectangle(10, 12, 1, 2, 5)
        Rectangle1.x = 20
        self.assertEqual(Rectangle1.x, 20)
        # Bad values/types
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle1.x = -20
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle1.x = "twenty"
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle1.x = 1.5
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle1.x = []
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle1.x = {}

    def test_9_y_setter(self):
        """
        Testing y setter.
        """
        Rectangle1 = Rectangle(10, 12, 1, 2, 5)
        Rectangle1.y = 20
        self.assertEqual(Rectangle1.y, 20)
        # Bad values/types
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle1.y = -20
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle1.y = "twenty"
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle1.y = 20.5
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle1.y = []
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle1.y = {}

    def test_10_area(self):
        """
        Testing area method.
        """
        Rectangle1 = Rectangle(10, 12, 1, 2, 5)
        rect_area = Rectangle1.area()
        self.assertTrue(type(rect_area) is int)
        self.assertEqual(rect_area, 120)

    def test_11_update(self):
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

    def test_12_to_dictionary(self):
        """
        Testing the to_dictionary method.
        """
        Rectangle1 = Rectangle(10, 10, 1, 2, 5)
        Rectangle1_dict = Rectangle1.to_dictionary()
        self.assertTrue(type(Rectangle1_dict) is dict)
        dict1 = {'id': 5, 'width': 10, 'height': 10, 'x': 1, 'y': 2}
        self.assertEqual(Rectangle1_dict, dict1)

    def test_13_Rectangle_save_to_file(self):
        """
        Testing Rectangle.save_to_file.
        """
        Rectangle1 = Rectangle(10, 12, 1, 2, 5)
        Rectangle.save_to_file([Rectangle1])
        with open("Rectangle.json", "r") as file:
            self.assertTrue(len(file.read()) == 54)
        # Passing None
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertTrue(len(file.read()) == 2)
        # Empty args
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertTrue(len(file.read()) == 2)

    def test_14_Rectangle_load_from_file(self):
        """
        Testing Rectangle.load_from_file.
        """
        Rectangle_list = Rectangle.load_from_file()
        self.assertTrue(type(Rectangle_list) is list)
        self.assertTrue(len(Rectangle_list) == 0)

if __name__ == "__main__":
    unittest.main()
