#!/usr/bin/python3
import urllib.request
import sys
"""to get the argyment passed"""
if len(sys.argv) < 2:
    print()

    """yene salliyiram duz olmadi"""
else:
    url = sys.argv[1]

    with urllib.request.urlopen(url) as res:
        print((res.headers()).get('X-Request-Id'))
    """duz olsa sevinerem salladim biraz"""
    """bu defe duzdu come on"""
