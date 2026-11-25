#!/usr/bin/python3
"""Defines a function that loads an object from a JSON file."""
import json


def load_from_json_file(filename):
    """Create an object from a JSON file.

    Args:
        filename (str): the name of the file to read.
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
