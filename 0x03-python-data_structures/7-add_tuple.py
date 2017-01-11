#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_a = list(tuple_a)
    list_b = list(tuple_b)

    if len(list_a) < 3:
        for i in range(2):
            list_a.append(0)
    if len(list_b) < 3:
        for i in range(2):
            list_b.append(0)

    a = list_a[0] + list_b[0]
    b = list_a[1] + list_b[1]

    res = (a, b)
    return res
