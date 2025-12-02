#!/usr/bin/python3
"""duzdu"""
import requests
import sys

if len(sys.argv) < 2:
    q = ''
else:
    q = sys.argv[1]
    try:
        response = requests.post(
            "http://0.0.0.0:5000/search_user",
            data={
                'q': q})
        r = response.json()
    except ValueError:
        print("Not a valid JSON")
    if r:
        print(f"[{r.get('id')}] {r.get('name')}")
    else:
        print("No result")
