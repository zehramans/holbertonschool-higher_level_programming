#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    b_dictionary = a_dictionary
    for i, j in b_dictionary.items():
        b_dictionary[i] = j*2
    return b_dictionary
