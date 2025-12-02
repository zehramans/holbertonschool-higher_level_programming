#!/usr/bin/python3
import requests
import sys
"""same thing but using reuqests"""
if len(sys.argv) < 2:
    print()
else:
    url = sys.argv[1]
    r = requests.get(url)
    print(r.headers['X-Request-Id'])
