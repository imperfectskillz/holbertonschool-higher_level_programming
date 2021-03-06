#!/usr/bin/python3
"""
Unnittest for Rectangle Class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRect(unittest.TestCase):

    def test_init(self):
        """empty"""
        with self.assertRaises(TypeError):
            new = Rectangle()

    def test_width(self):
        """test against arguments"""
        rect = Rectangle(5, 6, 9)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 6)
        self.assertEqual(rect.x, 9)
        self.assertEqual(rect.y, 0)
        self.assertEqual(rect.id, 0)

        rect2 = Rectangle(3, 5, 6, 11, 13)
        self.assertEqual(rect2.width, 3)
        self.assertEqual(rect2.height, 5)
        self.assertEqual(rect2.x, 6)
        self.assertEqual(rect2.y, 11)
        self.assertEqual(rect2.id, 13)

    def test_area(self):
        """
        tests area
        """
        a = Rectangle(1, 2)
        self.assertEqual(a.area(), 2)

    def test_width(self):
        """
        invalid type
        """
        with self.assertRaises(TypeError):
            a = Rectangle("1", 2)

    def test_value(self):
        """
        tests valid value
        """
        with self.assertRaises(ValueError):
            a = Rectangle(5, 0)
        with self.assertRaises(ValueError):
            a = Rectangle(0, 4)

    
