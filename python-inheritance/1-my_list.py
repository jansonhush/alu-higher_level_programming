#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""


class MyList(list):
    """A list that can print itself sorted."""

    def print_sorted(self):
        """Print the list sorted in ascending order.

        The list itself is not modified.
        """
        print(sorted(self))
