#!/usr/bin/python3

"""
Unittest BaseModel:
test_init
test_save
test_to_dict
"""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """"""
    def test_init(self):
        """"""
        obj = BaseModel()
        sizes = len(obj.id)
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)
        self.assertEqual(sizes, 36)
        self.assertNotEqual(obj.created_at, obj.updated_at)

    def test_save(self):
        """"""
        obj = BaseModel()
        time_created = obj.created_at
        obj.save()
        self.assertNotEqual(obj.updated_at, time_created)


if __name__ == '__main__':
    unittest.main()
