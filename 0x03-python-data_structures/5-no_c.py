#!/usr/bin/env python3
def no_c(my_string):
    my_list = []
    if my_string != []:
        for i in my_string:
            if (i != 'c' and i != 'C'):
                my_list.append(i)
    new_str = ("").join(my_list)
    return new_str
