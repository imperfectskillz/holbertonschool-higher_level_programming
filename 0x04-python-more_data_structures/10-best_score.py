#!/usr/bin/python3


def best_score(my_dict):
    if not my_dict:
        return None
    sort_dict = sorted(my_dict.values())
    for k, v in my_dict.items():
        if my_dict[k] == sort_dict[-1]:
            return k
