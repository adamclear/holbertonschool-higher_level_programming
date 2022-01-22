#!/usr/bin/python3
"""
This module contains the method: pascal_triangle.
"""


def pascal_triangle(n):
    """
    This method creates a Pascal Triangle of a particular
    size, 'n'.
    """
    if n <= 0:
        return []
    x = 0
    y = 0
    prev_row = []
    pascal_matrix = []
    while x < n:
        new_row = []
        y = 0
        while y < len(prev_row) + 1:
            if y == 0:
                ldigit = 0
            else:
                ldigit = prev_row[y - 1]
            if y == len(prev_row):
                rdigit = 0
            else:
                rdigit = prev_row[y]
            digit = ldigit + rdigit
            if digit == 0:
                digit = 1
            new_row.append(digit)
            y += 1
        pascal_matrix.append(new_row)
        x += 1
        prev_row = new_row
    return pascal_matrix
