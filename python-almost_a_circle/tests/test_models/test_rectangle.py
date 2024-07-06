#!/usr/bin/python3
"""Unit test for Rectangle"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO
import sys


class TestRectangle(unittest.TestCase):
    """
    TestRectangle class contains unit tests for the Rectangle class
    """

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_initialization(self):
        r1 = Rectangle(10, 20)
        r2 = Rectangle(2, 4, 1, 1, 42)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 20)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 4)
        self.assertEqual(r2.x, 1)
        self.assertEqual(r2.y, 1)
        self.assertEqual(r2.id, 42)

    def test_invalid_width(self):
        with self.assertRaises(TypeError):
            Rectangle("10", 20)
        with self.assertRaises(ValueError):
            Rectangle(-10, 20)
        with self.assertRaises(ValueError):
            Rectangle(0, 20)

    def test_invalid_height(self):
        with self.assertRaises(TypeError):
            Rectangle(10, "20")
        with self.assertRaises(ValueError):
            Rectangle(10, -20)
        with self.assertRaises(ValueError):
            Rectangle(10, 0)

    def test_invalid_x(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 20, "1")
        with self.assertRaises(ValueError):
            Rectangle(10, 20, -1)

    def test_invalid_y(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 20, 1, "1")
        with self.assertRaises(ValueError):
            Rectangle(10, 20, 1, -1)

    def test_area(self):
        r1 = Rectangle(10, 20)
        r1_area = r1.area()
        self.assertEqual(r1_area, 200)

    def test_display(self):
        r1 = Rectangle(4, 6)
        captured_output = StringIO()
        sys.stdout = captured_output
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "####\n####\n####\n####\n####\n####\n")

        r2 = Rectangle(2, 3, 1, 1)
        captured_output = StringIO()
        sys.stdout = captured_output
        r2.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "\n ##\n ##\n ##\n")

    def test_str(self):
        r1 = Rectangle(4, 6, 2, 3, 1)
        r2 = Rectangle(5, 7, 0, 0, 2)
        self.assertEqual(str(r1), "[Rectangle] (1) 2/3 - 4/6")
        self.assertEqual(str(r2), "[Rectangle] (2) 0/0 - 5/7")

    def test_update_args(self):
        r1 = Rectangle(2, 3)
        r1.update(10)
        self.assertEqual(r1.id, 10)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        r1.update(10, 15)
        self.assertEqual(r1.id, 10)
        self.assertEqual(r1.width, 15)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        r1.update(10, 15, 2)
        self.assertEqual(r1.id, 10)
        self.assertEqual(r1.width, 15)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        r1.update(10, 15, 2, 5)
        self.assertEqual(r1.id, 10)
        self.assertEqual(r1.width, 15)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 5)
        self.assertEqual(r1.y, 0)

        r1.update(10, 15, 2, 5, 7)
        self.assertEqual(r1.id, 10)
        self.assertEqual(r1.width, 15)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 5)
        self.assertEqual(r1.y, 7)

    def test_update_kwargs(self):
        r1 = Rectangle(2, 3)
        r1.update(id=10)
        self.assertEqual(r1.id, 10)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        r1.update(id=10, width=15)
        self.assertEqual(r1.id, 10)
        self.assertEqual(r1.width, 15)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        r1.update(id=10, width=15, height=2)
        self.assertEqual(r1.id, 10)
        self.assertEqual(r1.width, 15)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        r1.update(id=10, width=15, height=2, x=5)
        self.assertEqual(r1.id, 10)
        self.assertEqual(r1.width, 15)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 5)
        self.assertEqual(r1.y, 0)

        r1.update(id=10, width=15, height=2, x=5, y=7)
        self.assertEqual(r1.id, 10)
        self.assertEqual(r1.width, 15)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 5)
        self.assertEqual(r1.y, 7)

    def test_to_dictionary(self):
        r1 = Rectangle(10, 2, 1, 9, 1)
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(r1_dictionary, {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10})

if __name__ == '__main__':
    unittest.main()
