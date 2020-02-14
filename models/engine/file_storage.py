#!/usr/bin/env python3
''' Module contains the class Filestorage '''
import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        ''' Returns the dictionary __objects '''
        return self.__objects

    def new(self, obj):
        ''' sets in __objects the obj with key <obj class name>.id '''
        self.__objects["{}.{}".format(type(obj), obj.id)] = obj

    def save(self):
        ''' serializes __objects to the JSON file (path: __file_path) '''
        json_dict = {}
        for keys in FileStorage.__objects.keys():
            json_dict[keys] = FileStorage.__objects[keys].to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            f.write(json.dumps(json_dict))

    def reload(self):
        ''' deserializes the JSON file to __objects (if file exists) '''
        try:
            with open(FileStorage.__file_path, 'r') as f:
                FileStorage.__objects = json.loads(f.read())
        except:
            return
        for v in FileStorage.__objects.values():
            v = BaseModel(**v)


