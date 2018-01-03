#!/bin/usr/python3


def list_division(my_list_1, my_list_2, list_length):
    result = []
    i = 0
    while i < list_length:
        try:
            result.append(my_list_1[i] / my_list_2[i])
        except TypeError:
            print("wrong type")
            result.append(0)
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except IndexError:
            result.append(0)
            print("out of range")
        finally:
            i = i + 1
    return result
