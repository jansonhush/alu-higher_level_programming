#!/usr/bin/python3
"""Module for text_indentation function.

This module provides a function that prints text with two newlines
after '.', '?', and ':'.
"""


def text_indentation(text):
    """Print text with 2 new lines after each '.', '?', and ':'."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    buf = ""
    for ch in text:
        buf += ch
        if ch in ".?:":
            buf += "\n\n"

    lines = buf.split("\n")
    print("\n".join(line.strip(" ") for line in lines), end="")
