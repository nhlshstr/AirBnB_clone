#!/usr/bin/env python3
''' Module contains the class Filestorage '''
import json
import models
import models.base_model

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        ''' Returns the dictionary __objects '''
        return self.__objects

    def new(self, obj):
        ''' sets in __objects the obj with key <obj class name>.id '''
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        ''' serializes __objects to the JSON file (path: __file_path) '''
        json_dict = {}
        for keys in FileStorage.__objects.keys():
            json_dict[keys] = FileStorage.__objects[keys].to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            f.write(json.dumps(json_dict))

    def reload(self):
        ''' deserializes the JSON file to __objects (if file exists) '''
        json_dict = {}
        try:
            with open(FileStorage.__file_path, 'r') as f:
                json_dict = json.loads(f.read())
        except:
            return
        FileStorage.__objects = {}
        for keys in json_dict.keys():
            FileStorage.__objects[keys] = models.base_model.BaseModel(**json_dict[keys])
            


