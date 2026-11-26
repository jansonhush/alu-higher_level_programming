#!/usr/bin/python3
"""Module for print_square function.

This module provides a function that prints a square using '#'.
"""


def print_square(size):
    """Print a square with the character '#' of length size."""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
