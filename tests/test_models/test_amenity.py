#!/usr/bin/python3
''' Tests for amenity class '''
import unittest
from models.amenity import Amenity


class testAmenity(unittest.TestCase):
    ''' Tests the amenity class '''
    def test_type(self):
        ''' Tests type after creation '''
        a1 = Amenity()
        self.assertEqual(type(a1), Amenity)

    def testVariables(self):
        ''' Tests the class attributes that they exist '''
        a1 = Amenity()
        self.assertEqual(type(a1.name), str)
        self.assertEqual(u1.name, "")
