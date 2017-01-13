#!/usr/bin/python3
def best_score(my_dict):
    if my_dict == {} or my_dict is None:
        return None
    tmp = list(my_dict.values())
    tmp = tmp[0]
    for i in my_dict:
        if my_dict[i] >= tmp:
            tmp = my_dict[i]
            best = i
    return best
