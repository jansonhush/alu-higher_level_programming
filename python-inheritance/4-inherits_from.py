#!/usr/bin/python3
"""Defines a function that checks if an object inherits from a class."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a subclass of a_class.

    The object must come from a class that inherited (directly or
    indirectly) from a_class, but not be an instance of a_class itself.

    Args:
        obj: the object to check.
        a_class: the class to compare with.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
