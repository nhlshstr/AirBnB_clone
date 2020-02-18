#!/usr/bin/env python3
''' Module contains class User '''
from models.base_model import BaseModel


class User(BaseModel):
    ''' Class User description '''
    email = ""
    passowrd = ""
    first_name = ""
    last_name = ""
