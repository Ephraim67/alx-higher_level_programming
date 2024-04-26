#!/usr/bin/python3
"""
Function that devides 2 integers
"""


def safe_print_division(a, b):
    """
    Divides two integers and prints the result.

    Args:
        a (int): The dividend.
        b (int): The divisor.

    Returns:
        float or None: The result of the division.
    """
    try:
        result = a/b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result
