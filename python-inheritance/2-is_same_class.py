#!/usr/bin/python3
""" Biktik yav """


def is_same_class(obj, a_class):
    """ Def is so fun"""
    if obj == True or obj == False:
        return False
    return isinstance(obj, a_class)
