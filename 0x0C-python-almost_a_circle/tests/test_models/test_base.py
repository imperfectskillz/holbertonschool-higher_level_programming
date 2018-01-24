#!/usr/bin/python3
"""Unittest for Base Class"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    tests class Bass
    """

    def test_id(self):
        """
        tests id
        """
        a = Base()
        self.assertEqual(a.id, 1)

        b = Base()
        self.assertEqual(b.id, 5)

        c = Base(10)
        self.assertEqual(c.id, 10)
