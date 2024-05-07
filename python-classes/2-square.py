#!/usr/bin/python3
"""Module for class Square"""


class Square:
    """
    Definition of class Square
    Args:
        size (int): Size of Square
    """

    __size = 0

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
