#!/usr/bin/python3
"""Unit tests for Base class."""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test cases for Base class methods."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Remove temporary JSON files after each test."""
        for fname in ("Base.json", "Rectangle.json", "Square.json"):
            if os.path.exists(fname):
                os.remove(fname)

    def test_auto_and_custom_id(self):
        """Test automatic, explicit, zero, and negative IDs."""
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        b4 = Base(0)
        b5 = Base(-5)
        self.assertEqual((b1.id, b2.id, b3.id), (1, 12, 2))
        self.assertEqual((b4.id, b5.id), (0, -5))

    def test_to_and_from_json_string(self):
        """Test JSON string serialization and deserialization."""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])

        data = [{"id": 89, "width": 10, "height": 4}]
        json_str = Base.to_json_string(data)
        self.assertIsInstance(json_str, str)
        self.assertEqual(Base.from_json_string(json_str), data)

    def test_save_to_file_none_and_empty(self):
        """Test save_to_file with None and empty list."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r", encoding="utf-8") as f:
            self.assertEqual(f.read(), "[]")
        Square.save_to_file([])
        with open("Square.json", "r", encoding="utf-8") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_and_load_from_file(self):
        """Test saving and loading Rectangle and Square instances."""
        self.assertEqual(Rectangle.load_from_file(), [])
        self.assertEqual(Square.load_from_file(), [])

        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])
        rects = Rectangle.load_from_file()
        self.assertEqual([str(r) for r in rects], [str(r1), str(r2)])
        self.assertIsNot(rects[0], r1)

        s1 = Square(5, 0, 0, 1)
        s2 = Square(7, 9, 1, 2)
        Square.save_to_file([s1, s2])
        squares = Square.load_from_file()
        self.assertEqual([str(s) for s in squares], [str(s1), str(s2)])

    def test_create(self):
        """Test create class method for Rectangle and Square."""
        r = Rectangle.create(id=89, width=3, height=5, x=1, y=2)
        self.assertEqual(str(r), "[Rectangle] (89) 1/2 - 3/5")
        s = Square.create(id=42, size=6, x=2, y=3)
        self.assertEqual(str(s), "[Square] (42) 2/3 - 6")


if __name__ == "__main__":
    unittest.main()
