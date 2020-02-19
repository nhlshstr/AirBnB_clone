#!/usr/bin/env python3
"""Test module for city"""
import unittest
from models.city import City

class testCity(unittest.TestCase):
    """Class to test City"""
    def testType(self):
        """Tests if object is of specified class"""
        x1 = City()
        self.assertEqual(type(x1), City)

    def testName(self):
        """To check if name is of type string"""
        x1 = City()
        self.assertEqual(type(x1.name), str)
        self.assertEqual(x1.name, "")

    def testStateID(self):
        """To check if state ID is of type string"""
        x1 = City()
        self.assertEqual(type(x1.state_id, str)
        self.assertEqual(x1.state_id, "")
