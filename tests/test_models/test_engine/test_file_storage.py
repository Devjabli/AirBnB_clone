#!/usr/bin/python3

"""
Unittests for FileStorage class
"""
import os
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
        self.storage.__objects = {}
        self.base_model = BaseModel()
        self.user = User()
        self.storage.new(self.base_model)
        self.storage.new(self.user)

    def tearDown(self):
        """Tear down test methods"""
        self.storage.__objects = {}
        try:
            os.remove(self.storage._FileStorage__file_path)
        except FileNotFoundError:
            pass

    def test_all(self):
        """Test that all returns the __objects dictionary"""
        objects = self.storage.all()
        self.assertIn(f"BaseModel.{self.base_model.id}", objects)
        self.assertIn(f"User.{self.user.id}", objects)

    def test_new(self):
        """Test that new adds an object to __objects"""
        new_model = BaseModel()
        self.storage.new(new_model)
        self.assertIn(f"BaseModel.{new_model.id}", self.storage.all())

    def test_save(self):
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()
        self.storage.new(bm)
        self.storage.new(us)
        self.storage.new(st)
        self.storage.new(pl)
        self.storage.new(cy)
        self.storage.new(am)
        self.storage.new(rv)
        self.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + bm.id, save_text)
            self.assertIn("User." + us.id, save_text)
            self.assertIn("State." + st.id, save_text)
            self.assertIn("Place." + pl.id, save_text)
            self.assertIn("City." + cy.id, save_text)
            self.assertIn("Amenity." + am.id, save_text)
            self.assertIn("Review." + rv.id, save_text)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            self.storage.save(None)

    def test_reload(self):
        """Test that reload correctly deserializes JSON to __objects"""
        self.storage.save()
        self.storage.__objects = {}
        self.storage.reload()
        self.assertIn(f"BaseModel.{self.base_model.id}", self.storage.all())
        self.assertIn(f"User.{self.user.id}", self.storage.all())

if __name__ == '__main__':
    unittest.main()
