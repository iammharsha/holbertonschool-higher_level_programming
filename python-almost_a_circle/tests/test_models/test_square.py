#!/usr/bin/python3
"""Unit test for class Square"""
import unittest
from models.base import Base
from models.square import Square
from io import StringIO
import sys

class TestSquare(unittest.TestCase):
    """
    TestSquare class contains unit tests for the Square class
    """

    def setUp(self):
        Base._Base__nb_objects = 0
        self.s1 = Square(2)
        self.s2 = Square(3, 1)
        self.s3 = Square(4, 2, 1)
        self.s4 = Square(5, 1, 1, 15)

    def test_initialization(self):
        self.assertEqual(self.s1.size, 2)
        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s1.y, 0)
        self.assertEqual(self.s1.id, 1)
        self.assertEqual(self.s4.size, 5)
        self.assertEqual(self.s4.x, 1)
        self.assertEqual(self.s4.y, 1)
        self.assertEqual(self.s4.id, 15)

    def test_invalid_size(self):
        with self.assertRaises(TypeError):
            Square("10")
        with self.assertRaises(ValueError):
            Square(-10)
        with self.assertRaises(ValueError):
            Square(0)

    def test_invalid_x(self):
        with self.assertRaises(TypeError):
            Square(10, "1")
        with self.assertRaises(ValueError):
            Square(20, -1)

    def test_invalid_y(self):
        with self.assertRaises(TypeError):
            Square(20, 1, "1")
        with self.assertRaises(ValueError):
            Square(10, 1, -1)

    def test_area(self):
        s1_area = self.s1.area()
        self.assertEqual(s1_area, 4)
        s2_area = self.s2.area()
        self.assertEqual(s2_area, 9)
        s3_area = self.s3.area()
        self.assertEqual(s3_area, 16)
        s4_area = self.s4.area()
        self.assertEqual(s4_area, 25)

    def test_display(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.s1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "##\n##\n")

        captured_output = StringIO()
        sys.stdout = captured_output
        self.s4.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "\n #####\n #####\n #####\n #####\n #####\n")

    def test_str(self):
        self.assertEqual(str(self.s1), "[Square] (1) 0/0 - 2")
        self.assertEqual(str(self.s2), "[Square] (2) 1/0 - 3")
        self.assertEqual(str(self.s3), "[Square] (3) 2/1 - 4")
        self.assertEqual(str(self.s4), "[Square] (15) 1/1 - 5")

if __name__ == '__main__':
    unittest.main()
