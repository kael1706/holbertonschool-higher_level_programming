#!/usr/bin/python3
"""
This test is for the base class
Type: Unittest
Functions:
"""
import unittest
from models.base import Base as B
from models.rectangle import Rectangle as R
from models.square import Square as S

class t_base_class(unittest.TestCase):
    def test_id_input(self):
        """checking the entry of the id argument"""
        B._Base__nb_objects = 0

        b1 = B()
        self.assertEqual(b1.id, 1)

        b2 = B(17)
        self.assertEqual(b2.id, 17)

        b3 = B(-17)
        self.assertEqual(b3.id, -17)

    def test_id_plusplus(self):
        """checking the increase of the id argument"""
        B._Base__nb_objects = 0

        b4 = B()
        self.assertEqual(b4.id, 1)

        b5 = B()
        self.assertEqual(b5.id, 2)

        b6 = B()
        self.assertEqual(b6.id, 3)
        
        b7 = B(5)
        b8 = B()
        self.assertEqual(b8.id, 4)
        
        b9 = B()
        self.assertEqual(b9.id, 5)

    def test_to_json_string(self):
        """
        check JSON string representation of dictionary list.
        """
        r1 = R(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = B.to_json_string([dictionary])
        self.assertCountEqual(dictionary, {'x': 2, 'width': 10, 'id': 1,
                'height': 7, 'y': 8})
        self.assertEqual(type(dictionary), dict)
        self.assertEqual(type(json_dictionary), str)
