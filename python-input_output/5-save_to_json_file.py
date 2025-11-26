#!/usr/bin/python3
"""objecti deyir text fileina yaz deyir amma json kimi deyir"""


def save_to_json_file(my_obj, filename):
    """indi serialize elemek ucun dumps()
    istifade edecik bir de with open bayaqki"""
    import json
    with open(filename, "w", encoding="utf-8")as f:
        json.dump(my_obj, f)
        """dumps yox dump olurmus in this case"""
