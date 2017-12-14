#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    newa = tuple_a + (0, 0)
    newb = tuple_b + (0, 0)
    result1 = newa[0] + newb[0]
    result2 = newa[1] + newb[1]
    return result1, result2
