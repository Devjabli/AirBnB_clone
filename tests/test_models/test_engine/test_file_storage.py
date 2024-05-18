#!/usr/bin/python3
"""
Unittests for FileStorage class
"""
import unittest
import os
import json
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Tests for FileStorage class"""

    def setUp(self):
        """Set up test environment"""
        self.storage = FileStorage()
        self.file_path = self.storage._FileStorage__file_path
        if os.path.exists(self.file_path):
            os.rename(self.file_path, "tmp")

    def tearDown(self):
        """Clean up test environment"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        if os.path.exists("tmp"):
            os.rename("tmp", self.file_path)
        FileStorage._FileStorage__objects = {}

    def test_all_method(self):
        """Test all method"""
        self.assertEqual(self.storage.all(), {})

    def test_new_method(self):
        """Test new method"""
        user = User()
        self.storage.new(user)
        key = f"User.{user.id}"
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key], user)

    def test_save_method(self):
        """Test save method"""
        user = User()
        self.storage.new(user)
        self.storage.save()
        with open(self.file_path, "r", encoding='utf-8') as f:
            data = json.load(f)
            key = f"User.{user.id}"
            self.assertIn(key, data)
            self.assertEqual(data[key]["id"], user.id)

    def test_reload_method(self):
        """Test reload method"""
        user = User()
        self.storage.new(user)
        self.storage.save()
        FileStorage._FileStorage__objects = {}  # Clear objects
        self.storage.reload()
        key = f"User.{user.id}"
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key].id, user.id)

    def test_reload_no_file(self):
        """Test reload with no file"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        try:
            self.storage.reload()
            self.assertEqual(self.storage.all(), {})
        except Exception as e:
            self.fail(f"reload() raised {e} unexpectedly!")


if __name__ == "__main__":
    unittest.main()
