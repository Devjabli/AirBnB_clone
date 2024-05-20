#!/usr/bin/python3
"""
Defining FileStorage model to manipulate data to json
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    """
    Representing a storage engine

    Attributes private:
        __file_path (str): where objects saved to this file.
        __objects (dict): dictionary of objects.
    """


    __file_path = "file.json"
    __objects = {}
    class_map = {
        "BaseModel": BaseModel,
        "User": User,
        "Amenity": Amenity,
        "City": City,
        "Place": Place,
        "Review": Review,
        "State": State
    }

    def all(self):
        """ Returning the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """ Sets in __objects obj with key id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """ Serializing data __objects to JSON __file_path """
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump({key: value.to_dict() for key, value in self.__objects.items()}, f)

    def reload(self):
        """ Deserlializing JSON file from __file_path to __objects as dictionary"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                objdict = json.load(f)
                for obj_data in objdict.values():
                    class_name = obj_data["__class__"]
                    if class_name in self.class_map:
                        cls = self.class_map[class_name]
                        del obj_data["__class__"]
                        self.new(cls(**obj_data))
        except FileNotFoundError:
            pass
