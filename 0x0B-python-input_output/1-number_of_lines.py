#!/usr/bin/python3
"""
1-number_of_lines
"""


def number_of_lines(filename=""):
    """ reads file and counts the number of the lines in the file """
    count = 0
    with open(filename, encoding='UTF8') as f:
        for line in f:
            count += 1
    return count
