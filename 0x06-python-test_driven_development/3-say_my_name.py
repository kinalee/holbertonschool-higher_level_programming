#!/usr/bin/python3
"""
3-say_my_name
that prints "My name is " and two given arguments
Contains one module: say_my_name
"""


def say_my_name(first_name, last_name=""):
    """
    first_name and last_name should be strings
    """
    try:
        print("My name is {:s} {:s}".format(first_name, last_name))
    except:
        if isinstance(first_name, str) is not True:
            raise TypeError("first_name must be a string")
        if isinstance(last_name, str) is not True:
            raise TypeError("last_name must be a string")
