#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        count = 0
        for y in x:
            if count < len(x):
                print("{:d}".format(y), end=" ")
            else:
                print("{:d}".format(y), end="")
            count = count + 1
        print()
