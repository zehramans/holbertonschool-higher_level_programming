#!/usr/bin/python3
"""serialize deserialize again"""
import json


def serialize_and_save_to_file(data, filename):
    """serialize"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """deserialize"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.loads(f)
