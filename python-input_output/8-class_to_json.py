#!/usr/bin/python3
"""Defines a function that describes an object as a dictionary."""


def class_to_json(obj):
    """Return the dictionary description of an object, for JSON.

    Args:
        obj: an instance of a class with serializable attributes.
    """
    return obj.__dict__.copy()
