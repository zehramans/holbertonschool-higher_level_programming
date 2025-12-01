#!/usr/bin/python3
import requests
"""get request"""
resp = requests.get("https://intranet.hbtn.io/status")
print("\t- type: {}".format(type(resp)))
print("\t- content: {}".format(resp))
