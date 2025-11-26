#!/usr/bin/python3
"""writes string to a text file and returns the number of characters"""


def write_file(filename="", text=""):
    """birini de bura"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
