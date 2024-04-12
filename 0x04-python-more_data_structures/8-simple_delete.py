#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """A function tha deletes a key in a dictionary"""
    if a_dictionary is None:
        return None

    if key in a_dictionary:
        del(a_dictionary[key])
    return a_dictionary
