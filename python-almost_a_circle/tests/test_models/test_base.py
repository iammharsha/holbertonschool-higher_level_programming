#!/usr/bin/python3
"""Unit test for Base Class"""
import unittest
import json
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

    def test_to_json_string_none(self):
        """Test to_json_string with None."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        """Test to_json_string with an empty list."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_valid(self):
        """Test to_json_string with a valid list of dictionaries."""
        dict_list = [
            {'id': 1},
            {'id': 2}
        ]
        json_str = Base.to_json_string(dict_list)
        expected_str = json.dumps(dict_list)
        self.assertEqual(json_str, expected_str)

    def test_from_json_string_none(self):
        """Test from_json_string with None."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        """Test from_json_string with an empty string."""
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string_valid(self):
        """Test from_json_string with a valid JSON string."""
        json_string = '[{"id": 1}, {"id": 2}]'
        expected_output = [
            {"id": 1},
            {"id": 2}
        ]
        self.assertEqual(Base.from_json_string(json_string), expected_output)

if __name__ == '__main__':
    unittest.main()
