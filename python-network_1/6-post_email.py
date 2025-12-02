#!/usr/bin/python3
import requests
import sys

if len(sys.argv) < 3:
    print()

else:
    url = sys.argv[1]
    email = sys.argv[2]
    payload = {"email": email}
    r = requests.post(url, data=payload)
    print(f"Your email is: {email}")
