#!/usr/bin/python3
"""
Function that prints x elements of a list
"""

def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            print(i, end='')
            count += 1

    except IndexError:
        pass

    print()

    return count
