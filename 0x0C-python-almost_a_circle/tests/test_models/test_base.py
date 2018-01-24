#!/usr/bin/python3
"""Unittest class Base"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    tests class Bass
    """

    def id_test(self):
        """
        tests id
        """
        a = Base()
        self.assertEqual(a.id, 1)

        b = Base()
        self.assertEqual(b.id, 5)

        c = Base(10)
        self.assertEqual(c.id, 10)
