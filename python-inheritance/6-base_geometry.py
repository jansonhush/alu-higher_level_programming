#!/usr/bin/python3
"""Defines a class BaseGeometry with an unimplemented area method."""


class BaseGeometry:
    """Represents the base of a geometry."""

    def area(self):
        """Raise an Exception: area is not implemented here."""
        raise Exception("area() is not implemented")
