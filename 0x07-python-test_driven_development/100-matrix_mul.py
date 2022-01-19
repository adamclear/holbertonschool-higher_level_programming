#!/usr/bin/python3
"""
This module contains the function matrix_mul.
"""


def matrix_mul(m_a, m_b):
    """
    This function multiplies two matrices and returns the factored
    matrix. Matrices must be a list of lists of ints or floats.
    All rows should be of the same size. 'm_b' must have the same
    number of rows as 'm_a' has columns.
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    if not all(isinstance(x, list) for x in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(x, list) for x in m_b):
        raise TypeError("m_b must be a list of lists")

    if not m_a or not m_a[0]:
        raise ValueError("m_a can't be empty")
    if not m_b or not m_b[0]:
        raise ValueError("m_b can't be empty")

    prev_len = len(m_a[0])
    for x in range(len(m_a)):
        row_len = len(m_a[x])
        if prev_len != row_len:
            raise TypeError("each row of m_a must be of the \
same size")
        prev_len = row_len
    prev_len = len(m_b[0])
    for x in range(len(m_b)):
        row_len = len(m_b[x])
        if prev_len != row_len:
            raise TypeError("each row of m_b must be of the \
same size")

    if (len(m_a) != 0 and len(m_b) != 0) and (len(m_a) != len(m_b[0])):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for x in range(len(m_a)):
        col = 0
        row_result = []
        while col != len(m_b[0]):
            row, res = 0, 0
            for y in range(len(m_a[0])):
                if not isinstance(m_a[x][y], (int, float)):
                    raise TypeError("m_a should contain only \
integers or floats")
                if not isinstance(m_b[row][col], (int, float)):
                    raise TypeError("m_b should contain only \
integers or floats")
                res += m_a[x][y] * m_b[row][col]
                if row == len(m_b) - 1:
                    row_result.append(res)
                    col += 1
                    res, y = 0, 0
                row += 1
        result.append(row_result)
    return result
