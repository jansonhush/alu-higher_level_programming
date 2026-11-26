#!/usr/bin/python3
"""Unit tests for Base class."""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for Base class."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_id_assignment(self):
        """Test automatic and explicit ID assignment."""
        b1 = Base()
        b2 = Base()
        b3 = Base(89)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 89)

    def test_to_json_string(self):
        """Test Base.to_json_string with None, empty, and valid list."""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        res = Base.to_json_string([{"id": 12}])
        self.assertIsInstance(res, str)
        self.assertEqual(res, '[{"id": 12}]')

    def test_from_json_string(self):
        """Test Base.from_json_string with None, empty, and valid string."""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        res = Base.from_json_string('[{"id": 89}]')
        self.assertIsInstance(res, list)
        self.assertEqual(res, [{"id": 89}])


if __name__ == "__main__":
    unittest.main()
