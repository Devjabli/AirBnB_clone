#!/usr/bin/python3

"""
Unittests for FileStorage class
"""
import time
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State

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
        classes = [BaseModel, User, State, Place, City, Amenity, Review]
        for cls in classes:
            instance = cls()
        self.storage.new(instance)
        
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + classes[0].id, save_text)
            self.assertIn("User." + classes[1].id, save_text)
            self.assertIn("State." + classes[2].id, save_text)
            self.assertIn("Place." + classes[3].id, save_text)
            self.assertIn("City." + classes[4].id, save_text)
            self.assertIn("Amenity." + classes[5].id, save_text)
            self.assertIn("Review." + classes[6].id, save_text)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            self.storage.save(None)

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
