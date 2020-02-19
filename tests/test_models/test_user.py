#!/usr/bin/python3
''' Tests for user class '''
import unittest
from models.user import User


class testUser(unittest.TestCase):
    ''' Test user class '''
    def testType(self):
        ''' Tests type after creation '''
        u1 = User()
        self.assertEqual(type(u1), User)

    def testVariables(self):
        ''' Tests the class attributes that they exist '''
        u1 = User()
        self.assertEqual(type(u1.email), str)
        self.assertEqual(u1.email, "")
        self.assertEqual(type(u1.password), str)
        self.assertEqual(u1.password, "")
        self.assertEqual(type(u1.first_name), str)
        self.assertEqual(u1.first_name, "")
        self.assertEqual(type(u1.last_name), str)
        self.assertEqual(u1.last_name, "")
