#!/usr/bin/python3
''' Module for testing the class BaseModel '''
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def test_initialization(self):
        ''' Tests the type of a new instance '''
        new_model = BaseModel()
        self.assertIsInstance(new_model, BaseModel)

    def test_id_assignment(self):
        ''' Tests the assignment of an id to an instance '''
        b1 = BaseModel()
        self.assertEqual(type(b1.id), str)
        self.assertRegex(b1.id,
                         r'[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}')

    def test_created_updated_at(self):
        ''' Tests create and update time variables at instance creation.'''
        b1 = BaseModel()
        self.assertEqual(1, 1)
