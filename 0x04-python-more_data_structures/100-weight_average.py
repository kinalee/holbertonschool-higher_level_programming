#!/usr/bin/python3
def weight_average(my_list=[]):
    sum = 0
    div = 0
    if my_list == [] or my_list is None:
        return 0
    for i in my_list:
        mul = 1
        for j in i:
            mul *= j
        div += i[1]
        sum += mul
    return sum / div
