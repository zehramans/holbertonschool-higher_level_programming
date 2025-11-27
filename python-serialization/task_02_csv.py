#!/usr/bin/python3
"""qeseng kod"""
import csv
import json


def convert_csv_to_json(csvfilename):
    """0 komek tekce ozum yazdim"""
    try:
        with open(csvfilename, "r") as ff:
            reader = list(csv.DictReader(ff))
        with open("data.json", "w") as f:
            json.dump(reader, f)
    except FileNotFoundError:
        return False
