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
        # Add other models here as needed
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

