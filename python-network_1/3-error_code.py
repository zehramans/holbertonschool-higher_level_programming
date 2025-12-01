#!/usr/bin/python3
import urllib.request
import sys
"""to display error codes"""
if len(sys.argv) < 2:
    print()

else:
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as res:
            body = res.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
