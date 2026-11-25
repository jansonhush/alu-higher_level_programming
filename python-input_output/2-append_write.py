#!/usr/bin/python3
"""Defines a function that appends a string to a text file."""


def append_write(filename="", text=""):
    """Append a string at the end of a UTF8 text file.

    Args:
        filename (str): the name of the file (created if missing).
        text (str): the string to append.

    Returns:
        The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
