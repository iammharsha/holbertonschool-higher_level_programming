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

    def to_json(self):
        """
        Function to retrieve document representation of Student instance

        Returns:
            dict: Document representation of Student instance
        """
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }    
