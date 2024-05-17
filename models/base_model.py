#!/usr/bin/python3

"""

"""
import models
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """
    """
    def __init__(self, *args, **kwargs):
        """
        """
        if len(kwargs) == 0:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = value
    def save(self):
        """
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
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
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)