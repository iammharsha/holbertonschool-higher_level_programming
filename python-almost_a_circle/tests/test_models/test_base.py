#!/usr/bin/python3
"""Unit test for Base Class"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    TestBase class contains unit tests for the Base class

    Methods:
        setUp(self): Resets the class attribute __nb_objects before each test.
        test_no_id(self): Tests automatic id assignment when no id is provided.
        test_with_id(self): Tests id assignment when an id is provided.
        test_mixed_id(self): Tests a mix of automatic and provided id assignments.
    """

    def setUp(self):
        """Resets the class attribute __nb_objects before each test"""
        Base._Base__nb_objects = 0

    def test_no_id(self):
        """Tests automatic id assignment when no id is provided"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_with_id(self):
        """Tests id assignment when an id is provided"""
        b1 = Base(12)
        self.assertEqual(b1.id, 12)
        b2 = Base(123)
        self.assertEqual(b2.id, 123)

    def test_mixed_id(self):
        """Tests a mix of automatic and provided id assignments"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(12)
        self.assertEqual(b2.id, 12)
        b3 = Base()
        self.assertEqual(b3.id, 2)
        b4 = Base(24)
        self.assertEqual(b4.id, 24)

if __name__ == '__main__':
    unittest.main()
