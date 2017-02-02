#!/usr/bin/python3
"""
10-square
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class """
    def __init__(self, size):
        """ initializes instance attribute size"""
        super().__init__(size, size)
        self.__size = size
