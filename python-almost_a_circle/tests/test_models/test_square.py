#!/usr/bin/python3
"""Unit tests for Square class."""
import io
import unittest
from unittest.mock import patch
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for Square class."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_init_and_validation(self):
        """Test initialization, size setter, and validation."""
        s = Square(5, 1, 3, 10)
        self.assertEqual((s.id, s.size, s.x, s.y), (10, 5, 1, 3))
        s.size = 8
        self.assertEqual((s.width, s.height), (8, 8))
        with self.assertRaises(TypeError):
            Square("5")
        with self.assertRaises(ValueError):
            Square(0)
        with self.assertRaises(ValueError):
            Square(-3)
        with self.assertRaises(TypeError):
            s.size = "9"
        with self.assertRaises(ValueError):
            s.size = -2

    def test_methods(self):
        """Test area, __str__, display, update, and to_dictionary."""
        s = Square(2, 2, 1, 7)
        self.assertEqual(s.area(), 4)
        self.assertEqual(str(s), "[Square] (7) 2/1 - 2")
        with patch("sys.stdout", new=io.StringIO()) as out:
            s.display()
            self.assertEqual(out.getvalue(), "\n  ##\n  ##\n")
        s.update(1, 3, 4, 5)
        self.assertEqual(str(s), "[Square] (1) 4/5 - 3")
        s.update(size=7, id=89, y=1, x=12)
        self.assertEqual(str(s), "[Square] (89) 12/1 - 7")
        self.assertEqual(
            s.to_dictionary(),
            {"id": 89, "size": 7, "x": 12, "y": 1}
        )


if __name__ == "__main__":
    unittest.main()
