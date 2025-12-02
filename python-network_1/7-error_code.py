#!/usr/bin/python3
import requests
import sys

if len(sys.argv) < 2:
    print()

else:
    url = sys.argv[1]

    try:
        response = requests.get(url)
        body = response.text

        if response.status_code >= 400:
            print(f"Error code: {response.status_code}")
        else:
            print(body)
    except requests.RequestException:
        pass
