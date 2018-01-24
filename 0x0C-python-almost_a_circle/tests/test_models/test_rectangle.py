#!/usr/bin/python3
"""
Unnittest for Rectangle Class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRect(unittest.TestCase):
    """
    test cases for rectangle
    """
    def test_init(self):
        """empty"""
        with self.assertRaises(TypeError):
            new = Rectangle()

    def test
