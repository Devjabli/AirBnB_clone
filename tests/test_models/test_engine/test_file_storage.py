#!/usr/bin/python3
"""

"""
import json
import unittest
from uuid import uuid4
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    """
    class 
    """
    def setUp(self):
        """Set up test environment"""
        self.storage = FileStorage()
        self.model = BaseModel()
        # Reset __objects before each test
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        """
        testing all method from storage
        """
        storage = FileStorage()
        self.assertEqual(storage.all(), FileStorage._FileStorage__objects)
        obj = BaseModel()
        obj.id = str(uuid4)
        storage.new(obj)
        self.assertIn(f"BaseModel.{obj.id}", storage.all())

    def test_new(self):
        """Test the new method"""
        self.storage.new(self.model)
        key = f"{self.model.__class__.__name__}.{self.model.id}"
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key], self.model)

    def test_save(self):
         """Test the save method"""
        
    def test_reload(self):
        "Test for Reload"
    
if __name__ == '__main__':
    unittest.main()