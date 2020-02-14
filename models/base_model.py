#!/usr/bin/python3
"""This is a base class module"""

from models import storage
import uuid
import datetime


class BaseModel:
    """Base Class"""
    def __init__(self, *args, **kwargs):
        """Constructor"""
        if kwargs is not None and kwargs != {}:
            for key, value in kwargs.items():
                self.__dict__[key] = value
            self.__dict__["created_at"] = datetime.datetime.strptime(
                    self.__dict__["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            self.__dict__["updated_at"] = datetime.datetime.strptime(
                    self.__dict__["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")

        else:
            self.id = str(uuid.uuid4())
            """Time initialized in object format"""
            self.created_at = datetime.datetime.today()
            self.updated_at = datetime.datetime.today()
            storage.new(self)

    def __str__(self):
        """Str method overwritten"""
        return "[{}] ({}) {}".format(
                type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Method to update"""
        self.updated_at = datetime.datetime.today()
        storage.save()

    def to_dict(self):
        """Adds class name to __dict__"""
        self.__dict__['__class__'] = type(self).__name__
        """Times converted to string format"""
        self.__dict__["created_at"] = self.created_at.isoformat()
        self.__dict__["updated_at"] = self.updated_at.isoformat()
        return self.__dict__
