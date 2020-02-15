#!/usr/bin/python3
''' Module for testing the class FileStorage '''
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):

    '''
    def SetUp(self):
        FileStorage._FileStorage__objects = {}
    '''
    def all(self):
        ''' Tests that the all method returns a dictionary '''
        s1 = FileStorage()
        b1 = BaseModel()
        s.new(b1)
        temp = s.all()
        self.assertEqual(type(temp), dict)
    
    def test_new(self):
        ''' Test that the new function adds a key:value pair to __objects '''
        s = FileStorage()
        FileStorage._FileStorage__objects = {}
        b1 = BaseModel()
        s.new(b1)
        temp = s.all()
        self.assertEqual(len(s.all()), 1)
        FileStorage._FileStorage__objects = {}
        s.reload()
