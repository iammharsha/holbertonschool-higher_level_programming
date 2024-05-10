#!/usr/bin/python3
"""Module for class Square"""


class Square:
    """
    Definition of class Square
    Args:
        size (int): Size of Square
    """

    __size = 0
    __position = (0, 0)

    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if (not isinstance(position, tuple)
                or len(position) != 2
                or not all(isinstance(num, int) for num in position)
                or not all(num >= 0 for num in position)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """
        Retrieve the value of positon

        Returns:
            (int, int): Value of position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the value of position

        Args:
            value (int, int): Value of position
        """
        if (not isinstance(value, tuple)
                or len(value) != 2
                or not all(isinstance(num, int) for num in value)
                or not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Print the square of size using hash"""

        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__position[1]):
                print()
            for j in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
