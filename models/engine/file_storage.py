#!/usr/bin/python3

"""
"""
import os
import json
from models.base_model import BaseModel

class FileStorage:
    """
    """

    __file_path = "file.json"
    __objects = {}
    __class_map = {
        "BaseModel": BaseModel,
    }

    def all(self):
        """
        """
        return self.__objects
    
    def new(self, obj):
        """
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        """
        with open(self.__file_path, 'w') as f:
            json.dump({key: value.to_dict() for key, value in self.__objects.items()}, f)
    
    def reload(self):
        """"""
        if not os.path.exists(self.__file_path):
            return

        try:
            with open(self.__file_path, 'r') as f:
                objdict = json.load(f)
                for obj_data in objdict.values():
                    class_name = obj_data["__class__"]
                    if class_name in self.__class_map:
                        cls = self.__class_map[class_name]
                        del obj_data["__class__"]
                        self.new(cls(**obj_data))
        except FileNotFoundError:
            pass

