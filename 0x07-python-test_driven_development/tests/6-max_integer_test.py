#!/usr/bin/python3
"""
Module to test for the a midule 6-max_integer
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Test cases for max_integer()
    """

    def test_empty_list(self):
        result = max_integer([])
        self.assertIsNone(result)

    def test_single_element_list(self):
        result = max_integer([5])
        self.assertEqual(result, 5)

    def test_positive_numbers(self):
        result = max_integer([1, 2, 3, 4, 5])
        self.assertEqual(result, 5)
   
    def test_negative_numbers(self):
        result = max_integer([-1, -2, -3, -4, -5])
        self.assertEqual(result, -1)

    def test_mixed_num(self):
        res = max_integer([1, 2, -1, -10])
        self.assertEqual(res, 2)

    def test_empty_params(self):
        res = max_integer()
        self.assertIsNone(res)

    def test_param_list(self):
        a = [1, 2, 3]
        result = max_integer(a)
        self.assertIsInstance(a, list)
        self.assertIsInstance(result, int)
    