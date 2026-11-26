#!/usr/bin/python3
"""Unit tests for Rectangle class."""
import io
import os
import unittest
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Remove Rectangle.json if created."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

    def test_init_overloads(self):
        """Test Rectangle initialization with 2, 3, 4, and 5 arguments."""
        r1 = Rectangle(1, 2)
        r2 = Rectangle(1, 2, 3)
        r3 = Rectangle(1, 2, 3, 4)
        r4 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual((r1.width, r1.height, r1.x, r1.y), (1, 2, 0, 0))
        self.assertEqual((r2.x, r2.y), (3, 0))
        self.assertEqual((r3.x, r3.y), (3, 4))
        self.assertEqual(r4.id, 5)

    def test_init_exceptions(self):
        """Test TypeError and ValueError on Rectangle arguments."""
        for args in (("1", 2), (1, "2"), (1, 2, "3"), (1, 2, 3, "4")):
            with self.assertRaises(TypeError):
                Rectangle(*args)
        for args in ((-1, 2), (1, -2), (0, 2), (1, 0), (1, 2, -3), (1, 2, 3, -4)):
            with self.assertRaises(ValueError):
                Rectangle(*args)

    def test_area_str_display_dict(self):
        """Test area, __str__, display variants, and to_dictionary."""
        r = Rectangle(2, 2)
        self.assertEqual(r.area(), 4)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 2/2")
        with patch("sys.stdout", new=io.StringIO()) as out:
            r.display()
            self.assertEqual(out.getvalue(), "##\n##\n")
        with patch("sys.stdout", new=io.StringIO()) as out:
            Rectangle(2, 2, 1).display()
            self.assertEqual(out.getvalue(), " ##\n ##\n")
        with patch("sys.stdout", new=io.StringIO()) as out:
            Rectangle(2, 2, 1, 1).display()
            self.assertEqual(out.getvalue(), "\n ##\n ##\n")
        self.assertEqual(
            Rectangle(10, 2, 1, 9, 1).to_dictionary(),
            {"id": 1, "width": 10, "height": 2, "x": 1, "y": 9}
        )

    def test_update_and_create(self):
        """Test incremental *args, **kwargs, and Rectangle.create."""
        r = Rectangle(10, 10, 10, 10)
        r.update()
        r.update(89)
        r.update(89, 1)
        r.update(89, 1, 2)
        r.update(89, 1, 2, 3)
        r.update(89, 1, 2, 3, 4)
        self.assertEqual(str(r), "[Rectangle] (89) 3/4 - 1/2")
        r.update(**{"id": 89})
        r.update(**{"id": 89, "width": 1})
        r.update(**{"id": 89, "width": 1, "height": 2})
        r.update(**{"id": 89, "width": 1, "height": 2, "x": 3})
        r.update(**{"id": 89, "width": 1, "height": 2, "x": 3, "y": 4})
        self.assertEqual(str(r), "[Rectangle] (89) 3/4 - 1/2")
        for kw in (
            {"id": 89},
            {"id": 89, "width": 1},
            {"id": 89, "width": 1, "height": 2},
            {"id": 89, "width": 1, "height": 2, "x": 3},
            {"id": 89, "width": 1, "height": 2, "x": 3, "y": 4}
        ):
            self.assertEqual(Rectangle.create(**kw).id, 89)

    def test_save_to_file_none(self):
        """Test save_to_file(None)."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r", encoding="utf-8") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty(self):
        """Test save_to_file([])."""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r", encoding="utf-8") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_and_load(self):
        """Test save_to_file with instance and load_from_file."""
        self.assertEqual(Rectangle.load_from_file(), [])
        Rectangle.save_to_file([Rectangle(1, 2)])
        loaded = Rectangle.load_from_file()
        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0].id, 1)

if __name__ == "__main__":
    unittest.main()
