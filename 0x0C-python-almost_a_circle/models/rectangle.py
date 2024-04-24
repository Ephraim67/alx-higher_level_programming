#!/user/bin/python3
"""A class rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class that inherits from Base.

    Attributes:
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.
        x (int): x-coordinate of the top-left corner of the rectangle.
        y (int): y-coordinate of the top-left corner of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a Rectangle instance.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int, optional): x-coordinate of the top-left corner of the rectangle.
            y (int, optional): y-coordinate of the top-left corner of the rectangle.
            id (int, optional): ID of the rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """return the value of the width"""
        return self.__width

    @property
    def height(self):
        """return the value of the height"""
        return self.__height

    @property
    def x(self):
        """return the value of x"""
        return self.__x

    @property
    def y(self):
        """return the value of y"""
        return self.__y

    @width.setter
    def width(self, value):
        """set the value of the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """set the value of the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be >=0")
        self.__height = value

    @x.setter
    def x(self, value):
        """set the value of x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """set the value of y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
