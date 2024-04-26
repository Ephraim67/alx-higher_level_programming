#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """
    function that executes a function safely
    """

    try:
        result = fct(*args)
        return result
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
