#!/usr/bin/python3
def search_replace(my_list, search, replace):
    replaced = []
    for x in my_list:
        if x == search:
            x = replace
        replaced.append(x)
    return replaced
