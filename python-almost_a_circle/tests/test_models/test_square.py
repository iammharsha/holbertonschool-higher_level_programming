#!/usr/bin/python3
"""Unit test for class Square"""
import unittest
import json
import sys
import os
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

    def tearDown(self):
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass

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

    def test_save_to_file_none(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_empty(self):
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_valid(self):
        Square.save_to_file([self.s1, self.s3])
        with open("Square.json", "r") as file:
            content = file.read()
            list_dicts = [self.s1.to_dictionary(), self.s3.to_dictionary()]
            self.assertEqual(content, json.dumps(list_dicts))

    def test_create_square(self):
        s1_dict = {"id": 19}
        s1_obj = Square.create(**s1_dict)
        self.assertEqual(s1_obj.id, 19)
        self.assertEqual(s1_obj.size, 1)
        self.assertEqual(s1_obj.x, 0)
        self.assertEqual(s1_obj.y, 0)

        s2_dict = {"id": 19, "size": 4}
        s2_obj = Square.create(**s2_dict)
        self.assertEqual(s2_obj.id, 19)
        self.assertEqual(s2_obj.size, 4)
        self.assertEqual(s2_obj.x, 0)
        self.assertEqual(s2_obj.y, 0)

        s3_dict = {"id": 19, "size": 4, "x": 2}
        s3_obj = Square.create(**s3_dict)
        self.assertEqual(s3_obj.id, 19)
        self.assertEqual(s3_obj.size, 4)
        self.assertEqual(s3_obj.x, 2)
        self.assertEqual(s3_obj.y, 0)

        s4_dict = {"id": 19, "size": 4, "x": 2, "y": 7}
        s4_obj = Square.create(**s4_dict)
        self.assertEqual(s4_obj.id, 19)
        self.assertEqual(s4_obj.size, 4)
        self.assertEqual(s4_obj.x, 2)
        self.assertEqual(s4_obj.y, 7)

    def test_load_from_file_no_file(self):
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass
        squares = Square.load_from_file()
        self.assertEqual(squares, [])

    def test_load_from_file_exists(self):
        Square.save_to_file([self.s2, self.s3])

        squares = Square.load_from_file()
        self.assertEqual(len(squares), 2)
        self.assertEqual(squares[0].size, 3)
        self.assertEqual(squares[0].x, 1)
        self.assertEqual(squares[0].y, 0)
        self.assertEqual(squares[1].size, 4)
        self.assertEqual(squares[1].x, 2)
        self.assertEqual(squares[1].y, 1)

if __name__ == '__main__':
    unittest.main()
