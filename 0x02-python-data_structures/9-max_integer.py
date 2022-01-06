#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        max_int = my_list[0]
        for x in my_list:
            if x > max_int:
                max_int = x
        return max_int
    else:
        return None
