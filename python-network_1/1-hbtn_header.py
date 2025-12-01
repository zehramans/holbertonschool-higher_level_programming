#!/usr/bin/python3
import urllib.request 
import sys
"""to get the argyment passed"""

url = sys.argv[:1]

with urllib.request.urlopen(url) as res:
    a = (res.headers()).get('X-Request-Id')
    print(a)
    """duz olsa sevinerem salladim biraz"""
