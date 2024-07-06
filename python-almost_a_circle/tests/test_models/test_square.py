#!/usr/bin/python3
"""Unit test for class Square"""
import unittest
import json
import sys
from io import StringIO
from models.base import Base
from models.square import Square


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

    def test_update_args(self):
        self.s1.update(5)
        self.assertEqual(self.s1.id, 5)
        self.assertEqual(self.s1.size, 2)
        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s1.y, 0)

        self.s1.update(5, 3)
        self.assertEqual(self.s1.id, 5)
        self.assertEqual(self.s1.size, 3)
        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s1.y, 0)

        self.s1.update(5, 3, 6)
        self.assertEqual(self.s1.id, 5)
        self.assertEqual(self.s1.size, 3)
        self.assertEqual(self.s1.x, 6)
        self.assertEqual(self.s1.y, 0)

        self.s1.update(5, 8, 6, 10)
        self.assertEqual(self.s1.id, 5)
        self.assertEqual(self.s1.size, 8)
        self.assertEqual(self.s1.x, 6)
        self.assertEqual(self.s1.y, 10)

    def test_update_kwargs(self):
        self.s1.update(id=8)
        self.assertEqual(self.s1.id, 8)
        self.assertEqual(self.s1.size, 2)
        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s1.y, 0)

        self.s1.update(id=8, size=32)
        self.assertEqual(self.s1.id, 8)
        self.assertEqual(self.s1.size, 32)
        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s1.y, 0)

        self.s1.update(id=8, size=32, x=56)
        self.assertEqual(self.s1.id, 8)
        self.assertEqual(self.s1.size, 32)
        self.assertEqual(self.s1.x, 56)
        self.assertEqual(self.s1.y, 0)

        self.s1.update(id=8, size=32, x=56, y=28)
        self.assertEqual(self.s1.id, 8)
        self.assertEqual(self.s1.size, 32)
        self.assertEqual(self.s1.x, 56)
        self.assertEqual(self.s1.y, 28)

    def test_to_dictionary(self):
        s4_dictionary = self.s4.to_dictionary()
        self.assertEqual(s4_dictionary, {'x': 1, 'y': 1, 'id': 15, 'size': 5})

    def test_to_json_string(self):
        dict_list = [self.s1.to_dictionary(), self.s4.to_dictionary()]
        json_string = Base.to_json_string(dict_list)
        expected_json = json.dumps(dict_list)
        self.assertEqual(json_string, expected_json)

if __name__ == '__main__':
    unittest.main()
