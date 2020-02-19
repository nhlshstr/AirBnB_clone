#!/usr/bin/env python3
"""Test module for place"""
import unittest
from models.place import Place

class testCity(unittest.TestCase):
    """Class to test City"""
    def testType(self):
        """Tests if object is of specified class"""
        x1 = Place()
        self.assertEqual(type(x1), Place)

    def testName(self):
        """To check if name is of type string"""
        x1 = Place()
        self.assertEqual(type(x1.name), str)
        self.assertEqual(x1.name, "")

    def testCityID(self):
        """To check if city ID is of type string"""
        x1 = Place()
        self.assertEqual(type(x1.city_id, str)
        self.assertEqual(x1.state_id, "")

    def testUserID(self):
        """To check if user ID is of type string"""
        x1 = Place()
        self.assertEqual(type(x1.user_id, str)
        self.assertEqual(x1.user_id, "")

    def testDescription(self):
        """To check if description is of type string"""
        x1 = Place()
        self.assertEqual(type(x1.description, str)
        self.assertEqual(x1.description, "")
    
    def testNoRooms(self):
        """To check rooms"""
        x1 = Place()
        self.assertEqual(type(x1.number_rooms, int)
        self.assertEqual(x1.number_rooms, 0)
    
    def testNoBathRooms(self):
        """To check bathrooms"""
        x1 = Place()
        self.assertEqual(type(x1.number_bathrooms, int)
        self.assertEqual(x1.number_bathrooms, 0)
    
    def testMaxGuests(self):
        """To check max guests"""
        x1 = Place()
        self.assertEqual(type(x1.max_guests, int)
        self.assertEqual(x1.max_guests, 0)

    def testNightPrice(self):
        """To check nightly price"""
        x1 = Place()
        self.assertEqual(type(x1.price_by_night, int)
        self.assertEqual(x1.price_by_night, "")


    def testLatitude(self):
        """To check latitude"""
        x1 = Place()
        self.assertEqual(type(x1.latitude, float)
        self.assertEqual(x1.latitude, 0.0)

    def testLongitude(self):
        """To check longitude"""
        x1 = Place()
        self.assertEqual(type(x1.longitude, float)
        self.assertEqual(x1.longitude, 0.0)
