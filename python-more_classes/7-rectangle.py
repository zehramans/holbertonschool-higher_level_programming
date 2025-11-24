#!/usr/bin/python3
"""thast crazy"""


class Rectangle:
    """salam"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """aha"""
        number_of_instances += 1
        self.width = width
        self.__height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        a = ''
        if self.width == 0 or self.height == 0:
            return a

        for i in range(self.height):
            if i == self.height - 1:
                a = a + self.width * str(self.print_symbol)
            else:
                a = a + self.width * str(self.print_symbol) + "\n"
        return a

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.height})"

    def __del__(self):
        number_of_instances -= 1
        print("Bye rectangle...")
