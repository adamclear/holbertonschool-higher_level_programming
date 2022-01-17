#!/usr/bin/python3
"""
This module contains the function text_indentation.
"""


def text_indentation(text):
    """
    This function prints the given 'text', but inserts a blank
    line after every '.', '?', and ':'. 'text' must be a string.
    """
    y = 1
    buffer = ''
    limiters = ['.', '?', ':']
    if type(text) is not str:
        raise TypeError("text must be a string")
    for x in text:
        buffer = buffer + x
        if y == len(text) and x not in limiters:
            buffer = buffer.strip()
            print(buffer, end="")
        elif x in limiters:
            buffer = buffer.strip()
            print(buffer)
            print()
            buffer = ""
        y += 1
