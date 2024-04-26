#!/usr/bin/python3


def safe_print_integer_err(value):
    """function that prints and integer"""
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        print("Exception: {}".format(e))
        return False
