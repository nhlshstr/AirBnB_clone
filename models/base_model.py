#!/usr/bin/python3
"""This is a base class module"""


import uuid
import datetime


class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.today().isoformat()
        self.updated_at = datetime.datetime.today().isoformat()

    def __str__(self):
        return "[{}] ({}) {}".format(
                type(self).__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.datetime.today().isoformat()

    def to_dict(self):
        self.__dict__['__class__'] = type(self).__name__
        return self.__dict__
