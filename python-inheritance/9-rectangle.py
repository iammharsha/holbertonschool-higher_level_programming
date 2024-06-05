#!/usr/bin/python3
"""Class Rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculate Area of the rectangle

        Returns:
            int: Returns the area of the Rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return Rectangle information in specified format

        Returns:
            string: String containing rectangle information
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
