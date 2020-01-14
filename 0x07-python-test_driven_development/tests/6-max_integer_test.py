#!/usr/bin/python3
"""
This test is for module  6-max_integer
Type: Unittest
Functions: max_integer()
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_one(self):
        """
            test-1->max_integer()
            techniques: assertEqual
        """
        self.assertEqual(max_integer([8, 9, 10, 11, 12]), 12)
        self.assertEqual(max_integer([-2, -5, -6]), -2)
        self.assertEqual(max_integer([4, -2, 7, 8, 3, -6]), 8)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([0, 0, 0]), 0)
