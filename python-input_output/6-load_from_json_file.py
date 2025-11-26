#!/usr/bin/python3
"""json fileindan object yarat"""


def load_from_json_file(filename):
    """burda da load() nan eyni qaydada deserialize
    bu arada dumpa hem obj hem f specify edirdik cunki
    basqa filea yazirdi bu ise sadece load edir"""
    import json
    with open(filename, "w", encoding="utf-8") as f:
        return json.load(f)
