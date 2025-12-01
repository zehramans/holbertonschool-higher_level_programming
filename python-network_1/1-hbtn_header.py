#!/usr/bin/python3
import urllib.request
import sys
"""to get the argyment passed"""
if len(sys.argv) < 2:
    return
"""yene salliyiram duz olmadi"""
url = sys.argv[1]

with urllib.request.urlopen(url) as res:
    a = (res.headers()).get('X-Request-Id')
    print(a)
    """duz olsa sevinerem salladim biraz"""
