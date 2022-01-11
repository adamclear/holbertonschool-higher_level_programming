#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = []
    sum = 0
    for x in my_list:
        if x not in uniq_list:
            uniq_list.append(x)
    for x in uniq_list:
        sum += x
    return sum
