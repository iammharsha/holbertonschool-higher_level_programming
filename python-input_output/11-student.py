#!/usr/bin/python3
"""Class Student"""


class Student:
    """
    Definition of Class student

    Args:
        first_name (string): First Name of student
        last_name (String): Last Name of student
        age (int): Age of student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Function to retrieve document representation of Student instance

        Returns:
            dict: Document representation of Student instance
        """
        if attrs is None:
            return self.__dict__

        json_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                json_dict[attr] = getattr(self, attr)

        return json_dict

    def reload_from_json(self, json):
        """
        Function to replace all attributes of Student instance

        Args:
            json (dict): Dictionary to replace Student instance values
        """
        for key, value in json.items():
            setattr(self, key, value)
