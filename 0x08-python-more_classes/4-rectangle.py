#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """A class that defines a rectangle
    Args:
        width: represent the width of the rectangle
        height: represent the height of the rectangle
    Raises:
          TypeError: Size must be an integer
          ValueError: Size is less than zero
    """

    def __init__(self, width=0, height=0):
        """Initialize the Rectangle with the width and height"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Return the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >=0")
        self.__width = value

    @property
    def height(self):
        """Return the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""
        if not isinstance(self, value):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >=0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """Present a diagram of the rectangle defined for an object"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rectangle_str = ""
            for _ in range(self.__height):
                rectangle_str += '#' * self.__width + '\n'
            return rectangle_str.strip()

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"
