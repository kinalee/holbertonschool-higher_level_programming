#!/usr/bin/python3
def element_at(list, idx):
    if idx > len(list) or idx < 0 or list == []:
        return None
    return list[idx]
