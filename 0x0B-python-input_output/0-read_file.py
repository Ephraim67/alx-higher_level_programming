#!/usr/bin/python3
"""Function that reads a text file (UTF8)and print it to stdout"""

def read_file(filename=""):
    """function that reads a file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
