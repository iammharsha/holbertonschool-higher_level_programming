#!/usr/bin/python3
"""Definition and implementation of Class Rectangle"""


class Rectangle:
    """A class to represent Rectangle Object"""

    __width = 0
    __height = 0

    def __init__(self, width=0, height=0):
        """Constructor for class Rectangle"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Getter function for property width

        Returns:
            int: Value of width of Rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter function for property width

        Args:
            value (int): Value of width of Rectangle
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        Getter function for property height

        Returns:
            int: Value of height of Rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter function for property height

        Args:
            value (int): Value of height of Rectangle
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """
        Calculate the area of Rectangle

        Returns:
            int: Area of rectangle
        """

        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate the perimeter of Rectangle

        Returns:
            int: Perimeter of rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
