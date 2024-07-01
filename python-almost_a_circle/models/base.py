#!/usr/bin/python3
"""Base Class"""
import json


class Base:
    """Base Class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for Base class

        Args:
            id (int): Identifier Attribute
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Static Method to return JSON string from dictionary

        Args:
            list_dictionaries (list): A list of dictionaries

        Returns:
            str: JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Function to save JSON string to file

        Args:
            list_objs (list): List of instances who inherits Base
        """
        filename = f"{cls.__name__}.json"
        if list_objs is None:
            list_objs = []
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(list_dicts)
        with open(filename, "w") as file:
            file.write(json_string)
