#!/usr/bin/python3
"""Serializes and deserializes json files"""

import json
import os


class FileStorage():
    """serializes and deserializes json file"""
    __file_path = "HBNB_Listings.json"
    __objects = dict()

    def all(self):
        """returns dictionary of objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj"""
        obj2 = obj.to_dict()
        obj_key = str(obj2["__class__"])
        obj_key = obj_key + "." + obj2["id"]
        FileStorage.__objects[obj_key] = dict(obj2)

    def save(self):
        """serializes object to the json file"""
        with open(FileStorage.__file_path, 'w') as fh:
            fh.write(json.dumps([FileStorage.__objects]))

    def reload(self):
        """deserializes json file to __objects"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as fh:
                objs_str = fh.read()
            obj_lst = json.loads(objs_str)
            FileStorage.__objects = obj_lst[0]
