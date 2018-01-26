#!/usr/bin/python3
"""
Module contains unnittest for square
"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_init(self):
        """
        init
        """
        with self.assertRaises(TypeError):
            a = Square()

    def test_type(self):
        """
        tests types
        """
        with self.assertRaises(TypeError):
            a = Square("a")
        with self.assertRaises(TypeError):
            a = Square({})

    def test_value(self):
        """
        tests values
        """
        with self.assertRaises(ValueError):
            a = Square(-1, 0, 1)
        with self.assertRaises(ValueError):
            a = Square(1, -1, -1)

    def test_update(self):
        """
        tests update
        """
        a = Square(2)
        self.assertEqual(a.width, 2)
        self.assertEqual(a.height, 2)
