#!/usr/bin/python3
"""
2-read_lines.py
"""


def read_lines(filename="", nb_lines=0):
    """ opens and reads 'nb_lines' lines from file """
    count = 0
    with open(filename, encoding='UTF8') as f:

        for line in f:
            count += 1

        if (nb_lines <= 0) or (nb_lines >= count):
            nb_lines = count

        f.seek(0)
        while nb_lines > 0:
            print(f.readline(), end="")
            nb_lines -= 1
