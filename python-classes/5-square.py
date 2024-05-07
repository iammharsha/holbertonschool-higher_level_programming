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

    def area(self):
        """
        Calculate Area of Square

        Returns:
            int: Area of square
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Retrieve the value of size

        Returns:
            int: Size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the value of size

        Args:
            value (int): Size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Print the square of size using hash"""

        if self.__size == 0:
            print("")
        else:B
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")
