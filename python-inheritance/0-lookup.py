#!/usr/bin/python3
"""Function to return list of attributes and methods of an object"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object

    Parameters:
        obj: Object for which attributes and methods are to be looked up

    Returns:
        list: A list of attributes and methods of the object
    """

    return dir(obj)
