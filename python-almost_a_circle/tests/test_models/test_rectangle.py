#!/usr/bin/python3
"""Unit test for Rectangle"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    TestRectangle class contains unit tests for the Rectangle class

    Methods:
        setUp(self): Resets the class attribute __nb_objects before each test.
    """

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

if __name__ == '__main__':
    unittest.main()
