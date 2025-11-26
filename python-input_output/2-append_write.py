#!/usr/bin/python3
"""appends a string at the end of the text file"""


def append_write(filename="", text=""):
    """so w was to write and a is for append"""
    with open(filrname, "a", encoding="utf-8") as f:
        return f.write(text)
