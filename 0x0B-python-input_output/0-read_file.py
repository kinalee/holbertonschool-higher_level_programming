#!/usr/bin/python3
"""
0-read_file.py
"""


def read_file(filename=""):
    """ reads file and prints context"""
    with open(filename, encoding='UTF8') as f:
        print(f.read(), end="")
