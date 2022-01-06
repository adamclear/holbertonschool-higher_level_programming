#!/usr/bin/python3
def big_diff(my_list=[]):
    if len(my_list) == 0:
        return 0
    max_int = my_list[0]
    min_int = my_list[0]
    for x in my_list:
        if x > max_int:
            max_int = x
        if x < min_int:
            min_int = x
    bigdiff = max_int - min_int
    return bigdiff
