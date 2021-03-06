#!/usr/bin/python3
"""
8-rectangle
class that defines rectangle
"""


class Rectangle:
    """ Rectangle class """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ initializes instance attribute width and height """
        Rectangle.number_of_instances += 1
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
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        else:
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
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returns the bigger rectangle """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    def area(self):
        """ returns the area of rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ returns the perimeter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """ make object readable """
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        else:
            return '\n'.join(str(self.print_symbol) * self.__width
                             for i in range(self.__height))

    def __repr__(self):
        """ returns the string representation of the object """
        return '{:s}({:s}, {:s})'.format(self.__class__.__name__,
                                         self.__width, self.__height)

    def __del__(self):
        """ destructs method """
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')
