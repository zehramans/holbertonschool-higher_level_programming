#!/usr/bin/python3
"""rectangle to inherit from basegeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle"""

    def __init__(self, width, height):
        """bura da document """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """area calculator da """
        return self.__width * self.__height

    def __str__(self):
        """burda da deyirem ki classin adini verir ozunu cagirma"""
        name = str(self.__class__.__name__)
        a = str(self.__width)
        b = str(self.__height)
        return f"[{name}] {w}/{h}"
