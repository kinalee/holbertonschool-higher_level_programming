#!/usr/bin/python3
"""
9-rectangle
"""


class BaseGeometry:
    """ BaseGeometry class"""
    def area(self):
        """ raises an Exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ Rectangle class """
    def __init__(self, width, height):
        """ initializes instance attribute width and height """
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, self.__width, self.__height)

    def area(self):
        """ returns the area of current rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ makes object readable """
        return "[{}] {:d}/{:d}".format(__class__.__name__,
                                       self.__width, self.__height)
