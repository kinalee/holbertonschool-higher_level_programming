#!/usr/bin/python3
"""
6-rectangle
class that defines rectangle
"""


class Rectangle:
    number_of_instances = 0

    """ initializes instance attribute width and height """
    def __init__(self, width=0, height=0):
        type(self).number_of_instances += 1
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
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ retrieves height """
        return self.__height

    @height.setter
    def height(self, value):
        """
        - sets height
        - raise errors when value is not int or value is less than 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns the area of rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ returns the perimeter of the rectangle """
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """ make object readable """
        return "\n".join(("#" * self.__width for i in range(self.__height)))

    def __repr__(self):
        """ returns the string representation of the object """
        return "{}({}, {})".format(self.__class__.__name__,
                                   self.__width, self.__height)

    def __del__(self):
        type(self).number_of_instances -= 1
        """ destructs method """
        print("Bye rectangle...")
