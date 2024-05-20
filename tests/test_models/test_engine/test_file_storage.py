#!/usr/bin/python3

"""
Unittests for FileStorage class
"""

import unittest
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """Set up test methods"""
        self.storage = FileStorage()
        self.storage.clear_objects()
        self.base_model = BaseModel()
        self.user = User()
        self.storage.new(self.base_model)
        self.storage.new(self.user)

    def tearDown(self):
        """Tear down test methods"""
        self.storage.clear_objects()
        try:
            os.remove(self.storage._FileStorage__file_path)
        except FileNotFoundError:
            pass

    def test_all(self):
        """Test that all returns the __objects dictionary"""
        objects = self.storage.all()
        self.assertIn(f"BaseModel.{self.base_model.id}", objects)
        self.assertIn(f"User.{self.user.id}", objects)
        self.assertEqual(len(objects), 2)

    def test_new(self):
        """Test that new adds an object to __objects"""
        new_model = BaseModel()
        self.storage.new(new_model)
        self.assertIn(f"BaseModel.{new_model.id}", self.storage.all())
        self.assertEqual(len(self.storage.all()), 3)

    def test_save(self):
        """Test that save correctly serializes __objects to JSON"""
        self.storage.save()
        with open(self.storage._FileStorage__file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            self.assertIn(f"BaseModel.{self.base_model.id}", data)
            self.assertIn(f"User.{self.user.id}", data)
            self.assertEqual(len(data), 2)

    def test_reload(self):
        """Test that reload correctly deserializes JSON to __objects"""
        self.storage.save()
        self.storage.clear_objects()
        self.assertEqual(len(self.storage.all()), 0)
        self.storage.reload()
        self.assertIn(f"BaseModel.{self.base_model.id}", self.storage.all())
        self.assertIn(f"User.{self.user.id}", self.storage.all())
        self.assertEqual(len(self.storage.all()), 2)

if __name__ == '__main__':
    unittest.main()