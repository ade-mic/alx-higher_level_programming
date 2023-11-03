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

    def test_max_int(self):
        self.assertIsNone(max_integer())
        a = [1, 2, 3]
        result = max_integer(a)
        self.assertIsInstance(a, list)
        self.assertEqual(result, 3)
        self.assertIsInstance(result, int)
    