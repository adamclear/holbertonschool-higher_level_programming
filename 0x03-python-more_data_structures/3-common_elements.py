#!/usr/bin/python3
def common_elements(set_1, set_2):
    com_ele = []
    set1 = set(set_1)
    set2 = set(set_2)
    if (set1 & set2):
        com_ele.append(set1 & set2)
    return com_ele
