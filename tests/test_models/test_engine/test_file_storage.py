#!/usr/bin/python3
"""

import unittest
from datetime import datetime
from uuid import uuid4
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):

    def test_all(self):
        """
        """
        storage = FileStorage()
        self.assertEqual(storage.all(), FileStorage._FileStorage__objects)
        obj = BaseModel()
        obj.id = str(uuid4)
        storage.new(obj)
        self.assertIn(f"BaseModel.{obj.id}", storage.all())

    pass
    
if __name__ == '__main__':
    unittest.main()
"""