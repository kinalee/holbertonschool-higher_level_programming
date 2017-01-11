#!/usr/bin/python3
def new_in_list(list, idx, element):
    if idx < 0 or idx > len(list) - 1:
        return list

    newList = list.copy()
    newList[idx] = element
    return newList
