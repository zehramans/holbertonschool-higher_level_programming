#!/usr/bin/python3
"""calss square"""
Rectangle = __import__("9-rectangle.py").Rectangle


class Square(Rectangle):
    """square"""

    def __init__(self, size):
        """initialize new square"""
        self.integer_validation("size", size)
        self.__size = size

        super().__init__(size, size)
