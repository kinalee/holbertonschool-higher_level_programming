#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    my_list = []
    for row in matrix:
        inner_list = []
        for i in row:
            inner_list.append(i * i)
        my_list.append(inner_list)
    return my_list
