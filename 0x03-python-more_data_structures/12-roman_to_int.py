#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    value = 0
    tempval = 0
    if not roman_string:
        return 0
    for x in roman_string:
        if x in roman.keys():
            tempval = roman[x]
        if value < tempval:
            value = tempval - value
        elif tempval < value:
            value = tempval + value
    return value
