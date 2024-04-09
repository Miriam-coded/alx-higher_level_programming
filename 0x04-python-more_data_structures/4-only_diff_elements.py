#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    od_set = {i for i in set_1 ^ set_2}
    return od_set
