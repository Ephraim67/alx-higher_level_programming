#!/usr/bin/python
"""Function that creates an object from a JSON file"""
import json


def load_from_json_file(filename):
    """function that creates an object"""
    with open(filename) as f:
        return json.load(f)
