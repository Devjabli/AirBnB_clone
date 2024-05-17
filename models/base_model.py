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
