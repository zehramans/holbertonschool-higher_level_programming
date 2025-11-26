#!/usr/bin/python3
"""onject return elesin amma json str olsun"""


def from_json_string(my_str):
    """dumps() = python objectini serialize eliyir json stringine
    loads() = json stringini deserialize eliyir python objectine
    """
    import json
    return json.loads(my_str)
