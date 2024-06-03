#!/usr/bin/python3
"""Check if object is instance of class inherited from class."""


def inherits_from(obj, a_class):
    """
    Check if object is instance of class inherited from a_class.

    Args:
    obj: The object to check.
    a_class: The specified class to check against.

    Returns:
    bool: True if obj is instance of class inherited from a_class; else False
    """

    return isinstance(obj, a_class) and not type(obj) is a_class
