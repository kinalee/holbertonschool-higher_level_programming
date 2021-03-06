#!/usr/bin/python3
"""
2-rectangle
class that defines rectangle
"""


class Rectangle:
    """ Rectangle class"""
    def __init__(self, width=0, height=0):
        """ initializes instance attribute width and height """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ retrieves width """
        return self.__width

    @width.setter
    def width(self, value):
        """
        - sets width
        - raise errors when value is not int or value is less than 0
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """ retrieves height  """
        return self.__height

    @height.setter
    def height(self, value):
        """
        - sets height
        - raise errors when value is not int or value is less than 0
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0

        return (self.__width * 2) + (self.__height * 2)
