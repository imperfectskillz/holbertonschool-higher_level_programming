#!/usr/bin/python3
"""
max integer unittest
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_true_int(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([1, 2]), 2)

    def test_negative_int(self):
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([-1, -2, 33]), 33)

    def test_string(self):
        self.assertEqual(max_integer(["1", "2"]), "2")
