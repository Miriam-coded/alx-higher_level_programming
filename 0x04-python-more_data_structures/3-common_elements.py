#!/usr/bin/python3
def common_elements(set_1, set_2):
    c_set = {i for i in set_1 & set_2}

    return c_set
