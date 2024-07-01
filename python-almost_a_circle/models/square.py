#!/usr/bin/python3
"""Class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square inherited from Class Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor for Class Square

        Args:
            size (int): Size of square
            x (int): Attribute x of class Square
            y (int): Attribute y of class Sqaure
            id (int): Identifier for object of class Square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        String representation of object of class Square in format
        [Square] (<id>) <x>/<y> - <size>

        Returns:
            str: String representation of object of class Square
        """
        return (f"[Square] ({self.id}) {self.x}/{self.y} - "
                f"{self.width}")

    @property
    def size(self):
        """
        Getter function for attribute size of class Square

        Returns:
            size (int): Value of size of Square
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter function for attribute size of class Square

        Args:
            value (int): Size of square
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
