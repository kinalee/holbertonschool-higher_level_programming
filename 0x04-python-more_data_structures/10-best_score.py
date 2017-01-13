#!/usr/bin/python3
def best_score(my_dict):
    tmp = 0
    if my_dict is None:
        return None
    for i in my_dict:
        if my_dict[i] > tmp:
            tmp = my_dict[i]
            best = i
    return best
