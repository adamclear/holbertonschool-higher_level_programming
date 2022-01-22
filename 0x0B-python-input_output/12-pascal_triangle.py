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
    x = 1
    y = 1
    prev_row = [1]
    pascal_matrix = [[1]]
    while x < n:
        new_row = []
        while y < len(prev_row) + 1:
            try:
                ldigit = prev_row[y - 1]
            except Exception:
                ldigit = 0
            try:
                rdigit = prev_row[y + 1]
            except Exception:
                rdigit = 0
            digit = ldigit + rdigit
            if digit == 0:
                digit = 1
            new_row.append(digit)
            y += 1
        pascal_matrix.append(new_row)
        x += 1
        prev_row = new_row
    return pascal_matrix
