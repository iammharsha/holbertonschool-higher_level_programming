#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = list(map(lambda x: replace_func(x, search, replace), my_list))
    return new_list


def replace_func(x, s, r):
    if x == s:
        return r
    return x
