#!/usr/bin/python3
def print_reversed_list_integer(list=[]):
    list.reverse()
    for i in list:
        print("{:d}".format(i))
