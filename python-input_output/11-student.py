#!/usr/bin/python3
"""Defines a class Student that can be saved and reloaded."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student.

        Args:
            first_name (str): the first name.
            last_name (str): the last name.
            age (int): the age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary representation of the student.

        Args:
            attrs (list): if it is a list of strings, only the attributes
                whose names are in this list are returned. Otherwise all
                attributes are returned.
        """
        if (isinstance(attrs, list) and
                all(isinstance(name, str) for name in attrs)):
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """Replace the attributes of the student using a dictionary.

        Args:
            json (dict): attribute names and their new values.
        """
        for key, value in json.items():
            setattr(self, key, value)
