#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """A class of rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializing the rectangle class
        Args:
            width: represents the width of the rectangle
            height: represent the height of the rectangle
        Raises:
              TypeError: if size is not an integer
              ValueError: if size is less than zero
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an int")
        if value < 0:
            raise ValueError("width must be >=0")
        self.__width = value

    @property
    def height(self):
        """height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an int")
        if value < 0:
            raise ValueError("height must be >=0")
        self.__height = value

    def area(self):
        """the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = ""
        for _ in range(self.__height):
            rectangle_str += str(self.print_symbol) * self.__width + '\n'
        return rectangle_str.rstrip('\n')

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye Rectangle...")
        Rectangle.number_of_instances -= 1
