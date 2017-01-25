#!/usr/bin/python3
"""
1-rectangle
class that defines rectangle
"""


class Rectangle:
    """ Rectangle class """
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
        - raises errors when value is not int or value is less than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ retrieves height  """
        return self.__height

    @height.setter
    def height(self, value):
        """
        - sets height
        - raises errors when value is not int or value is less than 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
