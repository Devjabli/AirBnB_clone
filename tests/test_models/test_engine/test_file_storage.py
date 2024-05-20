#!/usr/bin/python3

"""
Unittests for FileStorage class
"""
import time
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
        """Test that save updates updated_at attribute"""
        old_updated_at = self.base_model.updated_at
        time.sleep(1)  # Sleep for a second to ensure the timestamp changes
        self.base_model.save()
        new_updated_at = self.base_model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertTrue(new_updated_at > old_updated_at)

        # Check that the object is saved in storage
        self.assertIn(f"BaseModel.{self.base_model.id}", self.storage.all())

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