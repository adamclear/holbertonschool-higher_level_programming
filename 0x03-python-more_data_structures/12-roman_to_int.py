#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    value, tempval, preval = 0, 0, 0
    if not roman_string or not isinstance(roman_string, str):
        return 0
    for x in roman_string:
        if x in roman.keys():
            tempval = roman[x]
            if preval < tempval:
                value = value - preval
                tempval = tempval - preval
            value += tempval
            preval = tempval
        else:
            return 0
    return value
