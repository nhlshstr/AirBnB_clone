#!/usr/bin/python3
''' Tests for review class '''
import unittest
from models.review import Review


class testReview(unittest.TestCase):
    ''' Test review class '''
    def testType(self):
        ''' Tests type after creation '''
        r1 = Review()
        self.assertEqual(type(r1), User)

    def testVariables(self):
        ''' Tests the class attributes that they exist '''
        r1 = Review()
        self.assertEqual(type(r1.place_id), str)
        self.assertEqual(r1.place_id, "")
        self.assertEqual(type(r1.user_id), str)
        self.assertEqual(r1.user_id, "")
        self.assertEqual(type(r1.text), str)
        self.assertEqual(r1.text, "")
