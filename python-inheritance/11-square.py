#!/usr/bin/python3
"""Class Square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Calculate Area of the square

        Returns:
            int: Returns the area of the Square
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Return Square information in specified format

        Returns:
            string: String containing square information
        """
        return f"[Square] {self.__size}/{self.__size}"
