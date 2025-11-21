#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    final = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            final += 1
    except IndexError:
        pass
    print()
    return final
