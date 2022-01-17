#!/usr/bin/python3
"""
This module contains the function matrix_divided.
"""


def matrix_divided(matrix, div):
    """
    This function divides each element of 'matrix' by the
    number given, 'div', and returns a new matrix consisting
    of the quotients as a float rounded to two decimal places.
    """
    matrix_redivided = []
    row_len = 0
    prev_row = len(matrix[0])
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        row_redivided = []
        row_len = len(row)
        if row_len != prev_row:
            raise TypeError("Each row of the matrix must have the same size")
        for column in row:
            if type(column) is not int and type(column) is not float:
                raise TypeError("\
matrix must be a matrix (list of lists) of integers/floats")
            else:
                row_redivided.append(round(column/div, 2))
        matrix_redivided.append(row_redivided)
        prev_row = row_len
    return matrix_redivided
