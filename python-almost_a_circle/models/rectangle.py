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

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
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
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
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
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Function to calculate Area of Rectangle

        Returns:
            int: Area of Rectangle
        """
        return self.__width * self.__height

    def display(self):
        """Function to Print Rectangle using #"""
        for _ in range(self.__height):
            print('#' * self.__width)

    def __str__(self):
        """
        Function to return Rectangle representation in fromat
        [Rectangle] (<id>) <x>/<y> - <width>/<height>

        Returns:
            string: Returns string representation of class
        """
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "
                f"{self.__width}/{self.__height}")
