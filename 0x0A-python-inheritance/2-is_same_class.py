#!/usr/bin/python3
"""
2-is_same_class
"""


def is_same_class(obj, a_class):
    """ returns True
    if the object is exactly an instance of the specified class
    """
    if type(obj) == a_class:
        return True
    else:
        return False
