#!/usr/bin/python3
"""
This module is a unittest for max_integer
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class test_max_integer(unittest.TestCase):
    """
    This is the testing class for max_integer
    """

    def test_mod_docstring(self):
        """
        This function tests if the module is documented.
        """
        mod_docstring = __import__('6-max_integer').__doc__
        self.assertTrue(len(mod_docstring) > 1)

    def test_func_docstring(self):
        """
        This function tests if max_integer is documented.
        """
        func_docstring = max_integer.__doc__
        self.assertTrue(len(func_docstring) > 1)

    def test_positive_integers(self):
        """
        This function tests max_integer with positive integers.
        """
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([1, 3, 2]), 3)
        self.assertEqual(max_integer([3, 1, 2]), 3)

    def test_negative_integers(self):
        """
        This function tests max_integer with negative integers.
        """
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_mixed_integers(self):
        """
        This function tests max_integer with +/- integers.
        """
        self.assertEqual(max_integer([-1, -5, 1, 5]), 5)

    def test_no_list(self):
        """
        This function tests max_integer with no list.
        """
        self.assertIsNone(max_integer())

    def test_non_integer(self):
        """
        This function tests max_integer with a non-integer (str) item.
        """
        self.assertRaises(TypeError, max_integer, [1, "two", 3],
                          msg="unorderable types: str() > int()")

    def test_one_element(self):
        """
        This function tests max_integer with a list of one element
        """
        self.assertEqual(max_integer([10]), 10)

if __name__ == "__main__":
    unittest.main()
