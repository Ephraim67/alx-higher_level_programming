#!/usr/bin/python3
"""function that writes Object to text file using json"""
import json


def save_to_json_file(my_obj, filename):
    """file that writes to json text file"""
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
