#!/usr/bin/python3
"""
This test is for the Rectangle class
Type: Unittest
Functions:
"""
import unittest
from models.base import Base as B
from models.rectangle import Rectangle as R
from models.square import Square as S


class t_Rectangle_class(unittest.TestCase):
    """Rectangle unit tests"""

    def test_id_input(self):
        """checking the entry of the id argument"""
        B._Base__nb_objects = 0

        r6 = R(6, 3)
        self.assertEqual(r6.id, 1)

        r7 = R(6, 3, 0, 0, 17)
        self.assertEqual(r7.id, 17)

        r8 = R(6, 3, 0, 0, -17)
        self.assertEqual(r8.id, -17)
    
    def test_id_plusplus(self):
        """checking the increase of the id argument"""
        B._Base__nb_objects = 0

        r9 = R(6, 3)
        self.assertEqual(r9.id, 1)

        r10 = R(6, 3)
        self.assertEqual(r10.id, 2)

        r11 = R(6, 3)
        self.assertEqual(r11.id, 3)
        
        r12 = R(6, 3, 0, 0, 5)
        r13 = R(6, 3)
        self.assertEqual(r13.id, 4)

        r14 = R(6, 3)
        self.assertEqual(r14.id, 5)

    def test_propertys(self):
        """"checking propertys"""
        r15 = R(6, 3)
        self.assertEqual(r15.width, 6)
        self.assertRaisesRegex(
                TypeError,
                'width must be an integer',
                R,
                'k', 3, 0, 0, 17
                )
        self.assertRaisesRegex(
                ValueError,
                'width must be > 0',
                R,
                -6, 3, 0, 0, 17
                )

        r16 = R(6, 3)
        self.assertEqual(r16.height, 3)
        self.assertRaisesRegex(
                TypeError,
                'height must be an integer',
                R,
                6, 'k', 0, 0, 17
                )
        self.assertRaisesRegex(
                ValueError,
                'height must be > 0',
                R,
                6, -3, 0, 0, 17
                )
