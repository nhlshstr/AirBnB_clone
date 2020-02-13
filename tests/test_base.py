#!/usr/bin/python3
''' Module for testing the class BaseModel '''
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def test_initialization(self):
        ''' Tests the type of a new instance '''
        new_model = BaseModel()
        self.assertEqual(type(new_model), BaseModel)
