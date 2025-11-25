#!/usr/bin/python3
"""sonuncu"""
Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """cagirdim"""

    def __init__(self, size):
        """initialization"""
        self.integer_validator("size", size)
        self.__size = size

        super().__init__(size, size)
