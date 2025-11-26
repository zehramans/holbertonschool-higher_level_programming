#!/usr/bin/python3
def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f


def pascal_triangle(n):
    if n <= 0:
        return []
    lists = []
    esaslist = []
    for i in range(n):
        for j in range(i + 1):
            lists.append(factorial(i) // (factorial(j) * factorial(i - j)))
        esaslist.append(lists)
        print(lists)
        lists = []


print(pascal_triangle(5))
