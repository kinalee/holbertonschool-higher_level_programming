#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        count = 0
        for j in matrix[i]:
            print("{:d}".format(j), end="")
            count += 1
            if count < len(matrix[i]):
                print(" ", end="")
        print("")
