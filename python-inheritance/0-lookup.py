#!/usr/bin/python3
"""Defines a function that lists the attributes of an object."""


def lookup(obj):
    """Return the list of available attributes and methods of an object.

    Args:
        obj: the object to inspect.
    """
    return dir(obj)
