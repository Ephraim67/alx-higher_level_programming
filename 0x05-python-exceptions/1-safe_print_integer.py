#!/usr/bin/python3
"""This function prints an integer"""


def safe_print_integer(value):
    """
    Prints an integer with "{:d}".format().

    Args:
        value: The value to print.

    Returns:
        bool: True if value is an integer and printed correctly, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except(ValueError, TypeError):
        return False
