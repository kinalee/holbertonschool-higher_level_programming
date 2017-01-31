#!/usr/bin/python3
"""
7-base_geometry
"""


class BaseGeometry:
    """ BaseGeometry class """
    def area(self):
        """ raises an Exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
