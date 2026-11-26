#!/usr/bin/python3
"""Unit tests for Square class."""
import os
import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for Square class."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Remove Square.json if created."""
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_init_overloads(self):
        """Test Square initialization with 1, 2, 3, and 4 arguments."""
        s1 = Square(1)
        s2 = Square(1, 2)
        s3 = Square(1, 2, 3)
        s4 = Square(1, 2, 3, 4)
        self.assertEqual((s1.size, s1.x, s1.y), (1, 0, 0))
        self.assertEqual((s2.x, s2.y), (2, 0))
        self.assertEqual((s3.x, s3.y), (2, 3))
        self.assertEqual(s4.id, 4)

    def test_init_exceptions(self):
        """Test TypeError and ValueError on Square arguments."""
        for args in (("1",), (1, "2"), (1, 2, "3")):
            with self.assertRaises(TypeError):
                Square(*args)
        for args in ((-1,), (1, -2), (1, 2, -3), (0,)):
            with self.assertRaises(ValueError):
                Square(*args)

    def test_str_and_dict(self):
        """Test __str__ and to_dictionary on Square."""
        s = Square(10, 2, 1, 1)
        self.assertEqual(str(s), "[Square] (1) 2/1 - 10")
        self.assertEqual(
            s.to_dictionary(),
            {"id": 1, "size": 10, "x": 2, "y": 1}
        )

    def test_update_and_create(self):
        """Test incremental *args, **kwargs, and Square.create."""
        s = Square(5)
        s.update()
        s.update(89)
        s.update(89, 1)
        s.update(89, 1, 2)
        s.update(89, 1, 2, 3)
        self.assertEqual(str(s), "[Square] (89) 2/3 - 1")
        s.update(**{"id": 89})
        s.update(**{"id": 89, "size": 1})
        s.update(**{"id": 89, "size": 1, "x": 2})
        s.update(**{"id": 89, "size": 1, "x": 2, "y": 3})
        self.assertEqual(str(s), "[Square] (89) 2/3 - 1")
        for kw in (
            {"id": 89},
            {"id": 89, "size": 1},
            {"id": 89, "size": 1, "x": 2},
            {"id": 89, "size": 1, "x": 2, "y": 3}
        ):
            self.assertEqual(Square.create(**kw).id, 89)

    def test_save_to_file_none(self):
        """Test save_to_file(None)."""
        Square.save_to_file(None)
        with open("Square.json", "r", encoding="utf-8") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty(self):
        """Test save_to_file([])."""
        Square.save_to_file([])
        with open("Square.json", "r", encoding="utf-8") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_and_load(self):
        """Test save_to_file with instance and load_from_file."""
        self.assertEqual(Square.load_from_file(), [])
        Square.save_to_file([Square(1)])
        loaded = Square.load_from_file()
        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0].id, 1)

if __name__ == "__main__":
    unittest.main()
