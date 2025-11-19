#!/usr/bin/python3

def no_c(my_string):
    final = ""
    for i in my_string:
        if (i.lower()) != "c":
            final += i
    return final


print(no_c("gaccagag"))
