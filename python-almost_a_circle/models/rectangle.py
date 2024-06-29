#!/usr/bin/python3
"""Class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle inherited from Base class"""

    __width = 0
    __height = 0
    __x = 0
    __y = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for class Rectangle

        Args:
            self: instance of the class Rectangle
            width (int): Value of width of Rectangle
            height (int): Value of height of Rectangle
            x (int): Value of attribute x
            y (int): Value of attribute y
            id (int): Identifier for class
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        Getter function for attribute width

        Returns:
            int: Width of Rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter function for attribure width

        Args:
            value (int): Value of width of Rectangle
        """
        self.__width = value

    @property
    def height(self):
        """
        Getter function for attribute height

        Returns:
            int: Height of Rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter function for attribure height

        Args:
            value (int): Value of height of Rectangle
        """
        self.__height = value

    @property
    def x(self):
        """
        Getter function for attribute x

        Returns:
            int: Attribute x of Rectangle
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter function for attribure x

        Args:
            value (int): Value of attribute x of Rectangle
        """
        self.__x = value

    @property
    def y(self):
        """
        Getter function for attribute y

        Returns:
            int: Attribute y of Rectangle
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter function for attribure y

        Args:
            value (int): Value of attribute y of Rectangle
        """
        self.__y = value
