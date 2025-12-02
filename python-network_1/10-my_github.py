#!/usr/bin/python3
import requests
import sys
"""to access github"""
if len(sys.argv) < 3:
    print()
else:
    username = sys.argv[1]
    passwd = sys.argv[2]

    url = "https://api.github.com/user"
    r = requests.get(url, headers={"Authorization": f"token {passwd}"})

    if r.status_code >= 400:
        print(None)
    else:
        print(r.json().get("id"))
