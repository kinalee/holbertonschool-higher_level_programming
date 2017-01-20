#!/usr/bin/python3
"""
4-print_square
Prints a square with the character #
Contains one module: print_square
"""


def print_square(size):
    """
    size must be an integer
    """
    if isinstance(size, int) is not True:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) is True and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print('#',end="")
        print("")
