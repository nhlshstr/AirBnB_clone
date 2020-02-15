#!/usr/bin/python3
''' Module for testing the class BaseModel '''
import unittest
import datetime
import time
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
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def test_created_updated_at(self):
        ''' Tests the format of the create/update_at variables creation.'''
        b1 = BaseModel()
        self.assertEqual(type(b1.created_at), datetime.datetime)
        self.assertEqual(type(b1.updated_at), datetime.datetime)
        self.assertRegex(b1.created_at.isoformat(),
                         r'\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d[.]\d{6}')
        self.assertRegex(b1.updated_at.isoformat(),
                         r'\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d[.]\d{6}')

    def test_save_method(self):
        ''' Tests the save method for correct time'''
        '''
        b1 = BaseModel()
        temp_time = b1.updated_at
        b1.save()
        self.assertNotEqual(b1.updated_at, temp_time)
        initial_time = b1.updated_at.isoformat()
        time.sleep(.1)
        b1.save()
        later_time = b1.updated_at.isoformat()
        time_passed = float(later_time[-8:]) - float(initial_time[-8:])
        self.assertTrue(bool(time_passed > .1))
        '''

    def test_created_at_time(self):
        ''' Tests that created_at method is assigning correct time '''
        b1 = BaseModel()
        time.sleep(.1)
        time_later = datetime.datetime.today().isoformat()
        time_earlier = float(b1.created_at.isoformat()[-8:])
        time_diff = float(time_later[-8:]) - time_earlier
        self.assertGreater(time_diff, .1)
        self.assertEqual(b1.created_at.isoformat()[0:-8], time_later[0:-8])

    def test_str_(self):
        ''' Tests the format of __str__ method '''
        b1 = BaseModel()
        first_13_char = str(b1)[0:13]
        self.assertEqual(first_13_char, "[BaseModel] (")

    def test_to_dict(self):
        ''' Tests the to_dict method '''
        b1 = BaseModel()
        b1_dict = b1.to_dict()
        self.assertEqual(type(b1_dict), dict)
        self.assertEqual(type(b1_dict["created_at"]), str)
        self.assertEqual(type(b1_dict["updated_at"]), str)
        self.assertRegex(b1_dict["created_at"],
                         r'\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d[.]\d{6}')
        self.assertRegex(b1_dict["updated_at"],
                         r'\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d[.]\d{6}')

    def test_instance_from_dict(self):
        b1 = BaseModel()
        b1_dict = b1.to_dict()
        b2 = BaseModel(**b1_dict)
        self.assertEqual(type(b2), BaseModel)
        self.assertEqual(type(b2.created_at), datetime.datetime)
