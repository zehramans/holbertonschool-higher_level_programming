#!/usr/bin/python3
import requests
"""get request"""
resp = requests.get("https://intranet.hbtn.io/status")
alo = resp.read()
print("Body response:")
print("\t- type: {}".format(type(alo)))
print("\t- content: {}".format(alo))
