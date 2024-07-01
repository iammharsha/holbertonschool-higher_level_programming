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
