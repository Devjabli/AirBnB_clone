#!/usr/bin/python3

""" Representing the BaseModel class. """

import uuid
from datetime import datetime
import models

class BaseModel:
    """ Representing the BaseModel of the console project. """

    def __init__(self, *args, **kwargs):

        """
        Initializer of BaseModel

        Args:
            *args (Tuple): unused.
            **kwargs (dict): key and value of attributes.
        """

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key in "created_at" or key in "updated_at":
                    self.__dict__[key] = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = value

    def save(self):
        """
        Updating the attribute updated_at with current time 
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        The dictionary of BaseModel return as instance
        """
        tdict = self.__dict__.copy()
        dt_attr = ["created_at", "updated_at"]
        for attrb in dt_attr:
            if attrb in tdict:
                tdict[attrb] = tdict[attrb].isoformat()
        tdict["__class__"] = self.__class__.__name__
        return tdict

    def __str__(self):
        """
        Return the string representation of the BaseModel instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
