#!/usr/bin/python3
import requests
"""get request"""
resp = requests.get("https://intranet.hbtn.io/status")
alo = resp.content()
print("Body response:")
print("\t- type: {}".format(type(alo)))
print("\t- content: {}".format(alo))
