#!/usr/bin/python3
"""Check if object is instance of or inherited from class"""


def is_kind_of_class(obj, a_class):
    """
    Check if object is instance of or inherited from class.

    Args:
    obj: The object to check.
    a_class: The specified class to check against.

    Returns:
    bool: True if obj is instance of or inherited from class; otherwise False.
    """

    return isinstance(obj, a_class)
