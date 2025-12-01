#!/usr/bin/python3
"""urllib only"""
import urllib.request

url = "https://intranet.hbtn.io/status"

with urllib.request.urlopen(url) as res:
    body = res.read()
"""safely open and close the request"""
print("Body response:")
print("\t- type: {}".format(type(body)))
print("\t- content: {}".format(body))
print("\t- utf8 content: {}".format(body.decode('utf-8')))
