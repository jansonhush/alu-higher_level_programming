#!/usr/bin/python3
"""Unit tests for Rectangle class."""
import io
import unittest
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_init_and_validation(self):
        """Test initialization, TypeError, and ValueError cases."""
        r = Rectangle(10, 2, 3, 4, 12)
        self.assertEqual((r.id, r.width, r.height, r.x, r.y), (12, 10, 2, 3, 4))
        with self.assertRaises(TypeError):
            Rectangle()
        for bad in ("2", 2.5, True, None, [1], {"a": 1}):
            with self.assertRaises(TypeError):
                Rectangle(bad, 2)
            with self.assertRaises(TypeError):
                Rectangle(2, bad)
            with self.assertRaises(TypeError):
                Rectangle(2, 2, bad, 0)
            with self.assertRaises(TypeError):
                Rectangle(2, 2, 0, bad)
        for bad in (0, -1):
            with self.assertRaises(ValueError):
                Rectangle(bad, 2)
            with self.assertRaises(ValueError):
                Rectangle(2, bad)
        with self.assertRaises(ValueError):
            Rectangle(2, 2, -1, 0)
        with self.assertRaises(ValueError):
            Rectangle(2, 2, 0, -1)

    def test_methods(self):
        """Test area, __str__, display, update, and to_dictionary."""
        r = Rectangle(2, 3, 2, 2, 7)
        self.assertEqual(r.area(), 6)
        self.assertEqual(str(r), "[Rectangle] (7) 2/2 - 2/3")
        with patch("sys.stdout", new=io.StringIO()) as out:
            r.display()
            self.assertEqual(out.getvalue(), "\n\n  ##\n  ##\n  ##\n")
        r.update(89, 4, 5, 1, 0)
        self.assertEqual(str(r), "[Rectangle] (89) 1/0 - 4/5")
        r.update(y=3, width=6, id=10)
        self.assertEqual(str(r), "[Rectangle] (10) 1/3 - 6/5")
        self.assertEqual(
            r.to_dictionary(),
            {"id": 10, "width": 6, "height": 5, "x": 1, "y": 3}
        )


if __name__ == "__main__":
    unittest.main()
