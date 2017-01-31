#!/usr/bin/python3
"""
11-square
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


class Square(Rectangle):
    """ Square class """
    def __init__(self, size):
        """ initializes instance attribute size"""
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """ makes object readable  """
        return "[{}] {:d}/{:d}".format(__class__.__name__,
                                       self.__size, self.__size)
