#!/usr/bin/python3
"""
Defining FileStorage model to manipulate data to json.
"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    """
    Represents a storage engine for saving and loading data in JSON format.

    Attributes (private):
        __file_path (str): Path to the file where objects are saved.
        __objects (dict): Dictionary of objects currently in storage.
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

    def all(self) -> dict:
        """
        Returns the dictionary __objects.
        """
        return self.__objects

    def new(self, obj: BaseModel) -> None:
        """
        Adds a new object to __objects with a key formatted as <class name>.<id>.

        Args:
            obj (BaseModel): The object to be added.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self) -> None:
        """
        Serializes __objects to a JSON file specified by __file_path.
        """
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(
                {key: value.to_dict() for key, value in self.__objects.items()},
                f, indent=4
            )

    def reload(self) -> None:
        """
        Deserializes the JSON file specified by __file_path to __objects.

        If the file does not exist, it does nothing.
        """
        if os.path.exists(self.__file_path):
            try:
                with open(self.__file_path, 'r', encoding='utf-8') as f:
                    objdict = json.load(f)
                    for obj_data in objdict.values():
                        class_name = obj_data.get("__class__")
                        if class_name in self.class_map:
                            cls = self.class_map[class_name]
                            obj_data.pop("__class__", None)
                            self.new(cls(**obj_data))
            except json.JSONDecodeError:
                print("Error decoding JSON file. File might be corrupted.")
            except Exception as e:
                print(f"Unexpected error occurred: {e}")
        else:
            print("No file found to reload data.")
