#!/usr/bin/env python3
def no_c(my_string):
    new_str = ""
    if my_string != []:
        for i in my_string:
            if (i != 'c' and i != 'C'):
                new_str += i
    return new_str
