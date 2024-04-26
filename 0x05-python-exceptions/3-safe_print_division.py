#!/usr/bin/python3
"""Function that devides 2 integers and prints the results"""

def safe_print_division(a, b):
    """
    Divides two integers and prints the result.

    Args:
        a (int): The dividend.
        b (int): The divisor.

    Returns:
        float or None: The result of the division if successful, None otherwise.
    """
    try:
        result = a / b

    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result

