#!/usr/bin/python3
"""
salam
"""


def inherits_from(obj, a_class):
    """sehv olmaz da yeqin"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
