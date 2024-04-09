#!/usr/bin/python3
"""A class that defines a rectangle base by private instance attributes"""


class Rectangle:
    # A class that defines a rectangle

    def __init__(self, width, height):
        # Initialize the Rectangle instance with width and height.
        self.__width = width
        self.__height = height

    @property
    def width(self):
        # Retrive the width of the rectangle
        return (self.__width)

    @width.setter
    def width(self, value):
        # Set the Width of the Rectangle
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__width = value

    @property
    def height(self):
        # Retrieve the height of the rectangle
        return (self.__height)

    @height.setter
    def height(self, value):
        # Set the Height of the Rectangle
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
