#!/usr/bin/python3

def element_at(my_list, idx, new_element):
    if idx < 0 or idx >= len(my_list):
        return my_list[:]
    else:
        new_list = my_list[:]
        new_list[idx] = new_element
        return new_list
