#!/usr/bin/python3
"""Definition and implementation of Class Rectangle"""


class Rectangle:
    """A class to represent Rectangle Object"""

    __width = 0
    __height = 0
    number_of_instances = 0
    print_symbol = '#'

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
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """
        Return rectangle using hashes

        Returns:
            string: Rectangle shape using hashes(#)
        """

        s = ""
        if self.__width == 0 or self.__width == 0:
            return s

        for i in range(self.__height):
            s += str(self.print_symbol) * self.__width
            if i != self.__height - 1:
                s += '\n'

        return s

    def __repr__(self):
        """
        Return string representation of Rectangle

        Returns:
            string: String representation of Rectangle
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Clean up function when Rectangle object is deleted
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the biggest Rectangle based on area of two rectangle

        Returns:
            Rectangle: Instance of Class Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
