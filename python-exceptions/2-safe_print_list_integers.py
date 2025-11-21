#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    final = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                final += 1
    except IndexError:
        raise IndexError
    finally:
        print()
    return final
