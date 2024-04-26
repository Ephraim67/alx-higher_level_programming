#!/usr/bin/python3
"""
Function that prints x elements of a list
"""


def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print(f"{my_list[i]}", end="")
            count += 1

        except IndexError:
            pass

    print()

    return (count)
