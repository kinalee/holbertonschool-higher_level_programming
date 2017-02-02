#!/usr/bin/python3
"""
11-square
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class """
    def __init__(self, size):
        """ initializes instance attribute size"""
        BaseGeometry.integer_validator(self, "size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """ makes object readable  """
        return "[{}] {:d}/{:d}".format(__class__.__name__,
                                       self.__size, self.__size)
