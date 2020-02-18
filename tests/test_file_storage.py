#!/usr/bin/env python3
''' Module for testing the class FileStorage '''
import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):

    jPath = ""
    x1 = FileStorage()

    def setUp(self):
        """Creates new file storage class when a test runs"""
        FileStorage._FileStorage__objects = {}
        TestFileStorage._jPath = FileStorage._FileStorage__file_path
        FileStorage._FileStorage__file_path = "sample.json"

    def tearDown(self):
        """Removes sample.json file"""
        try:
            os.remove("sample.json")
        except:
            pass
        FileStorage._FileStorage__file_path = TestFileStorage.jPath


    def testAllReturn(self):
        ''' Tests that the all method returns a dictionary '''
        s1 = FileStorage()
        b1 = BaseModel()
        s1.new(b1)
        temp = s1.all()
        self.assertEqual(type(temp), dict)

    def testObjectMatch(self):
        """ Checks all() method """
        myDict = {"BaseModel.555":{"this":25, "be": 255},
                "BaseModel.666":{"the":44, "end": 55}}
        FileStorage._FileStorage__objects = myDict
        self.assertEqual(myDict, TestFileStorage.x1.all())


    def testNew(self):
        ''' Test that the new function adds a key:value pair to __objects '''
        s = FileStorage()
        FileStorage._FileStorage__objects = {}
        b1 = BaseModel()
        s.new(b1)
        temp = s.all()
        self.assertEqual(len(s.all()), 1)
        FileStorage._FileStorage__objects = {}
        s.reload()
