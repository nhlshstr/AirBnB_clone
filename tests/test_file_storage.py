#!/usr/bin/python3
''' Module for testing the class FileStorage '''
import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):

    jPath = ""

    def SetUp(self):
        """Creates new file_storage when a test runs"""
        FileStorage._FileStorage__objects = {}
        TestFileStorage._jPath = FileStorage._FileStorage__file_path
        FileStorage._FileStorage__file_path = "sample.json"

    def Destroy(self):
        """Removes sample.json file"""
        try:
            os.remove("sample.json")
        except:
            pass
        FileStorage._FileStorage__file_path = TestFileStorage.jPath


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


