#!/usr/bin/python3
"""
10-square
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class """
    def __init__(self, width, height):
        """ initializes instance attribute width and height """
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ returns the area of current rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ makes object readable """
        return "[{:s}] {:d}/{:d}".format(__class__.__name__,
                                         self.__width, self.__height)

class Square(Rectangle):
    """ Square class """
    def __init__(self, size):
        """ initializes instance attribute size"""
        super().__init__(size, size)
        self.__size = size
