#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    a = (tuple_a + (0, 0))[:2]
    b = (tuple_b + (0, 0))[:2]
    return tuple(x + y for x, y in zip(a, b))
