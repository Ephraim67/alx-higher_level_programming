#!/usr/bin/python3
"""A class of rectangle"""


class Rectangle:
    """This is a rectangle
    Args:
        width: represent the width of the rectangle
        height: represent the height of the rectangle
    Raises:
          TypeError: If size is not an integer
          ValueError: if size is less than 0
    """

    def __init__(self, width=0, height=0):
        """Initialize the Rectangle instance with width and height"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Return the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the Width of the Rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >=0")

    @property
    def height(self):
        """Return the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >=0")

    def area(self):
        """Returns the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rectangle_str = ""
            for _ in range(self.__height):
                rectangle_str += '#' * self.__width + '\n'
            return rectangle_str.strip()
