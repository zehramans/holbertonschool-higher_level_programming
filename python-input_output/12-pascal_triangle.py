#!/usr/bin/python3
"""salam"""


def factorial(n):
    """Return factorial of n (simple iterative version)"""
    if n == 0:
        return 1
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f


def pascal_triangle(n):
    """salam"""
    if n <= 0:
        return []
    esaslist = []
    for i in range(n):
        lists = []
        for j in range(i + 1):
            lists.append(factorial(i) // (factorial(j) * factorial(i - j)))
        esaslist.append(lists)
    return esaslist
