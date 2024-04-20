#!/usr/bin/python
"""

This function add two integer

"""


def add_integer(a, b=98):
    """Return the sum of two integers or float as integers

    Parameters:
             a: first arguments
             b: second arguments

    Raises:
           TypeError: if 'a' or 'b' is not an integer or float

    Returns:
          int: The sum of 'a' and 'b', casted to an integer

    """

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))

    a = int(a) if isinstance(a, float) else a
    b = int(b) if isinstance(b, float) else b
