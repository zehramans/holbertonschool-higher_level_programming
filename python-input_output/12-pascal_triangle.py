#!/usr/bin/python3
"""salam"""


def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f
    """slaam"""


def pascal_triangle(n):
    """salam"""
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
