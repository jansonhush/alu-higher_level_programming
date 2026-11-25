#!/usr/bin/python3
"""Defines a function that writes a string to a text file."""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file, replacing its content.

    Args:
        filename (str): the name of the file (created if missing).
        text (str): the string to write.

    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
