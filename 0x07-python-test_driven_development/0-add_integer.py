#!/usr/bin/python3
"""
Module add-integer
adds two integers
"""


def add_integer(a, b=98):
    """
    This function returns the sum of two integers and
    cast float into integers before summing
    """

    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")

    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)

    return a + b
