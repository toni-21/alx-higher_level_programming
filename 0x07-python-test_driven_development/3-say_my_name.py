#!/usr/bin/python3
"""
Module say_my_name
prints my name
"""


def say_my_name(first_name, last_name=""):
    """
    Print Full Name of a person.
    """
    if type(first_name) != str:
        raise TypeError('First_name must be a string')
    if type(last_name) != str:
        raise TypeError('Last_name must be a string')
    print("My name is " + first_name + " " + last_name)
