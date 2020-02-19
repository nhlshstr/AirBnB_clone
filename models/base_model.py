#!/usr/bin/python3
"""This is a base class module"""

import datetime
import models
import uuid


class BaseModel:
    """Base Class"""
    def __init__(self, *args, **kwargs):
        """Constructor"""
        if kwargs is not None and kwargs != {}:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.datetime.\
                            strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.updated_at = datetime.datetime.\
                            strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key is not "__class__":
                    self.__dict__[key] = value

        else:
            self.id = str(uuid.uuid4())
            """Time initialized in object format"""
            self.created_at = datetime.datetime.today()
            self.updated_at = datetime.datetime.today()
            models.storage.new(self)

    def __str__(self):
        """Str method overwritten"""
        return "[{}] ({}) {}".format(
                type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Method to update"""
        self.updated_at = datetime.datetime.today()
        models.storage.save()

    def to_dict(self):
        """Adds class name to __dict__"""
        dict_all = {}
        dict_all["__class__"] = type(self).__name__
        """Times converted to string format"""
        for k, v in self.__dict__.items():
            if k == "created_at":
                dict_all["created_at"] = self.created_at.isoformat()
            elif k == "updated_at":
                dict_all["updated_at"] = self.updated_at.isoformat()
            else:
                dict_all[k] = v
        return dict_all
