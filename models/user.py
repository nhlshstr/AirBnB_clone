#!/usr/bin/env python3
''' Module contains class User '''
from models.base_model import BaseModel


class User(BaseModel):
    ''' Class User description '''

    email = ""
    password = ""
    first_name = ""
    last_name = ""
