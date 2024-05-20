#!/usr/bin/python3

"""
Unittests for FileStorage class
"""

import os
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorageInstantiation(unittest.TestCase):
    """Tests for FileStorage instantiation."""

    def test_instantiation_no_args(self):
        self.assertIsInstance(FileStorage(), FileStorage)

    def test_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_private_file_path_str(self):
        self.assertIsInstance(FileStorage._FileStorage__file_path, str)

    def test_private_objects_dict(self):
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)

    def test_storage_initializes(self):
        from models import storage
        self.assertIsInstance(storage, FileStorage)


class TestFileStorageMethods(unittest.TestCase):
    """Tests for FileStorage methods."""

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDownClass(cls):
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def setUp(self):
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_all(self):
        from models import storage
        self.assertIsInstance(storage.all(), dict)

    def test_all_with_arg(self):
        from models import storage
        with self.assertRaises(TypeError):
            storage.all(None)

    def test_new(self):
        from models import storage
        instances = [BaseModel(), User(), State(), Place(), City(), Amenity(), Review()]
        for instance in instances:
            storage.new(instance)
            key = f"{instance.__class__.__name__}.{instance.id}"
            self.assertIn(key, storage.all().keys())
            self.assertIn(instance, storage.all().values())

    def test_new_with_args(self):
        from models import storage
        with self.assertRaises(TypeError):
            storage.new(BaseModel(), 1)

    def test_new_with_none(self):
        from models import storage
        with self.assertRaises(AttributeError):
            storage.new(None)

    def test_save(self):
        from models import storage
        instances = [BaseModel(), User(), State(), Place(), City(), Amenity(), Review()]
        for instance in instances:
            storage.new(instance)
        storage.save()
        with open("file.json", "r") as f:
            save_text = f.read()
            for instance in instances:
                self.assertIn(f"{instance.__class__.__name__}.{instance.id}", save_text)

    def test_save_with_arg(self):
        from models import storage
        with self.assertRaises(TypeError):
            storage.save(None)

    def test_reload(self):
        from models import storage
        instances = [BaseModel(), User(), State(), Place(), City(), Amenity(), Review()]
        for instance in instances:
            storage.new(instance)
        storage.save()
        storage.reload()
        objs = FileStorage._FileStorage__objects
        for instance in instances:
            self.assertIn(f"{instance.__class__.__name__}.{instance.id}", objs)

    def test_reload_with_arg(self):
        from models import storage
        with self.assertRaises(TypeError):
            storage.reload(None)


if __name__ == "__main__":
    unittest.main()
