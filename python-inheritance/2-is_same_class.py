#!/usr/bin/python3
""" Module to check if an object is exactly an instance of specified class"""


def is_same_class(obj, a_class):
    """
    Check if an object is exaclty an instance of specified class

    Args:
    obj: The object to check.
    a_class: The specified class to check against.

    Returns:
    bool: True if object is an instance of specified class; otherwise False.
    """

    return type(obj) is a_class
