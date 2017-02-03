#!/usr/bin/python3
"""
4-append_write
"""


def append_write(filename="", text=""):
    """
    appends a string at the end of the file
    and returns the number of characters added
    """
    with open(filename, 'a', encoding='UTF8') as f:
        return f.write(text)
