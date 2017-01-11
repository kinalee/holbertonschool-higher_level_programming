#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list == []:
        print("")
    else:
        list.reverse()
        for i in list:
            print("{:d}".format(i))
