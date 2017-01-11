#!/usr/bin/python3
def no_c(my_string):
    my_list = list()
    new_str = ""
    if my_string is not None:
        for i in my_string:
            if i is not 'c' and i is not 'C':
                my_list.append(i)
        new_str = ("").join(my_list)
        return new_str
