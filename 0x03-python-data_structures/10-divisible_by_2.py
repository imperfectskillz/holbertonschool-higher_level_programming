#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    new = []
    for i in my_list:
        new += [i % 2 == 0]
    return new
