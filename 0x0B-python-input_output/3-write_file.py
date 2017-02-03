#!/usr/bin/python3
"""
3-write_file
"""


def write_file(filename="", text=""):
    """
    writes a string to file
    and returns the number of characters written
    """
    with open(filename, 'w', encoding='UTF8') as f:
        return f.write(text)
