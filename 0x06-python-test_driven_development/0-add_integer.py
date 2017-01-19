#!/usr/bin/python3
"""
0-add_integer
Adds 2 integers and returns the sum
Contains one module: add_integer
"""


def add_integer(a, b):
    """
    Both a and b must be integers, a TypeError will be raise otherwise
    """
    try:
        return (int(a) + int(b))
    except:
        if isinstance(a, (int, float)) is not True:
            raise TypeError("a must be an integer")
        if isinstance(b, (int, float)) is not True:
            raise TypeError("b must be an integer")
