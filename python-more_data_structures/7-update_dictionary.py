#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    upd = {key: value}
    a_dictionary.update(upd)
    for i, j in a_dictionary.items():
        print("{}: {}".format(i, j))
