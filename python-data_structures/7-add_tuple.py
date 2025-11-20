#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) > len(tuple_b):
        for i in range (len(tuple_a)-len(tuple_b)):
            tuple_b+=(0, )
    else:
        for i in range (len(tuple_b)-len(tuple_a)):
            tuple_a+=(0, )
    return tuple(sum(pair) for pair in zip((tuple_a), (tuple_b)))

