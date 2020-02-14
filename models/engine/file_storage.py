#!/usr/bin/env python3
''' Module contains the class Filestorage '''

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        ''' Returns the dictionary __objects '''
        ...

    def new(self, obj):
        ''' sets in __objects the obj with key <obj class name>.id '''
        ...

    def save(self):
        ''' serializes __objects to the JSON file (path: __file_path) '''
        ...

    def reload(self):
        ''' deserializes the JSON file to __objects (if file exists) '''
        ...

