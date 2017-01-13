2#!/usr/bin/python3
def update_dictionary(my_dict, key, value):
    for i in my_dict.keys():
        if i == key:
            my_dict[i] = value
    if key not in my_dict: 
        my_dict[key] = value
    return my_dict
