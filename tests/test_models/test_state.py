#!/usr/bin/env python3
"""Test module for state"""
import unittest
from models.state import State


class testState(unittest.TestCase):
    """Class to test state"""
    def testType(self):
        """Tests if object is of specified class"""
        x1 = State()
        self.assertEqual(type(x1), State)

    def testName(self):
        """To check if name is of type string"""
        x1 = State()
        self.assertEqual(type(x1.name), str)
        self.assertEqual(x1.name, "")
