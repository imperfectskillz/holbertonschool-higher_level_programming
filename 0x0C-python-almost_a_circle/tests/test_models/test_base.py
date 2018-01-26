#!/usr/bin/python3
"""Unittest for Base Class"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_id(self):
        """
        tests id
        """
        a = Base()
        self.assertEqual(a.id, 1)
        b = Base()
        self.assertEqual(b.id, 5)
        c = Base()
        self.assertEqual(c.id, 10)

    def test_with_value(self):
        """
        given value
        """
        a = Base(4)
        self.assertEqual(a.id, 4)

    def test_string(self):
        """
        tests with string
        """
        a = Base("333")
        self.assertEqual(a.id, "333")
