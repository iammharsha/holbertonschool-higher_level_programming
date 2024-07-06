#!/usr/bin/python3
"""Unit test for Rectangle"""
import unittest
import json
import os
from io import StringIO
import sys
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    TestRectangle class contains unit tests for the Rectangle class
    """

    def setUp(self):
        Base._Base__nb_objects = 0

    def tearDown(self):
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass

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

    def test_to_json_string(self):
        r1 = Rectangle(10, 2, 1, 9, 1)
        r2 = Rectangle(5, 4)
        dict_list = [r1.to_dictionary(), r2.to_dictionary()]
        json_string = Base.to_json_string(dict_list)
        expected_string = json.dumps(dict_list)
        self.assertEqual(json_string, expected_string)

    def test_save_to_file_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_empty(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_valid(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            content = file.read()
            list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
            self.assertEqual(content, json.dumps(list_dicts))

    def test_create_rectangle(self):
        r1_dict = {"id": 1}
        r1_rect = Rectangle.create(**r1_dict)
        self.assertEqual(r1_rect.id, 1)
        self.assertEqual(r1_rect.width, 1)
        self.assertEqual(r1_rect.height, 1)
        self.assertEqual(r1_rect.x, 0)
        self.assertEqual(r1_rect.y, 0)

        r2_dict = {"id": 1, "width": 5}
        r2_rect = Rectangle.create(**r2_dict)
        self.assertEqual(r2_rect.id, 1)
        self.assertEqual(r2_rect.width, 5)
        self.assertEqual(r2_rect.height, 1)
        self.assertEqual(r2_rect.x, 0)
        self.assertEqual(r2_rect.y, 0)

        r3_dict = {"id": 1, "width": 5, "height": 3}
        r3_rect = Rectangle.create(**r3_dict)
        self.assertEqual(r3_rect.id, 1)
        self.assertEqual(r3_rect.width, 5)
        self.assertEqual(r3_rect.height, 3)
        self.assertEqual(r3_rect.x, 0)
        self.assertEqual(r3_rect.y, 0)

        r4_dict = {"id": 1, "width": 5, "height": 3, "x": 4}
        r4_rect = Rectangle.create(**r4_dict)
        self.assertEqual(r4_rect.id, 1)
        self.assertEqual(r4_rect.width, 5)
        self.assertEqual(r4_rect.height, 3)
        self.assertEqual(r4_rect.x, 4)
        self.assertEqual(r4_rect.y, 0)

        r5_dict = {"id": 1, "width": 5, "height": 3, "x": 4, "y": 7}
        r5_rect = Rectangle.create(**r5_dict)
        self.assertEqual(r5_rect.id, 1)
        self.assertEqual(r5_rect.width, 5)
        self.assertEqual(r5_rect.height, 3)
        self.assertEqual(r5_rect.x, 4)
        self.assertEqual(r5_rect.y, 7)

    def test_load_from_file_no_file(self):
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass
        r1 = Rectangle.load_from_file()
        self.assertEqual(r1, [])

    def test_load_from_file_exists(self):
        r1 = Rectangle(10, 5, 0, 1, 12)
        r2 = Rectangle(3, 4)
        Rectangle.save_to_file([r1, r2])
        
        rectangles = Rectangle.load_from_file()
        self.assertEqual(len(rectangles), 2)
        self.assertEqual(rectangles[0].width, 10)
        self.assertEqual(rectangles[0].height, 5)
        self.assertEqual(rectangles[0].x, 0)
        self.assertEqual(rectangles[0].y, 1)
        self.assertEqual(rectangles[1].width, 3)
        self.assertEqual(rectangles[1].height, 4)
        self.assertEqual(rectangles[1].x, 0)
        self.assertEqual(rectangles[1].y, 0)

if __name__ == '__main__':
    unittest.main()
