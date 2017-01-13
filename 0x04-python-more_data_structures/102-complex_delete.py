#!/usr/bin/python3
def complex_delete(my_dict, value):
    my_list = list()
    if value == ():
        return
    for key, val in my_dict.items():
        if val == value:
            my_list.append(key)
    for i in my_list:
        del my_dict[i]
    return my_dict
