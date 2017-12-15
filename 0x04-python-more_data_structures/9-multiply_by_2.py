#!/usr/bin/python3


def multiply_by_2(my_dict):

    new = my_dict.copy()
    for k, v in new.items():
        new[k] = v*2
    return new
