#!/usr/bin/python3

import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    final = 0
    for i in range(len(args)):
        final += int(args[i])
    print(final)
