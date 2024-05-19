#!/usr/bin/python3

"""
Unittest BaseModel:
test_init
test_save
test_to_dict
"""


import unittest
from datetime import datetime
from uuid import uuid4 
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ TestBaseModel for testing this class """
    def setUp(self):
        """
        Sets up the test methods
        """
        self.instance = BaseModel()
        self.instance_with_kwargs = BaseModel(id=str(uuid4()), created_at=datetime.now().isoformat(), updated_at=datetime.now().isoformat())

    def tearDown(self):
        """
        Clean up after test
        """
        del self.instance
        del self.instance_with_kwargs

    def test_creation(self):
        """
        Test creation of a new instance of BaseModel
        """
        self.assertIsInstance(self.instance, BaseModel)
        self.assertIsInstance(self.instance.id, str)
        self.assertIsInstance(self.instance.created_at, datetime)
        self.assertIsInstance(self.instance.updated_at, datetime)

    def test_creation_with_kwargs(self):
        """
        Test creation of a new instance of BaseModel with kwargs
        """
        self.assertIsInstance(self.instance_with_kwargs, BaseModel)
        self.assertIsInstance(self.instance_with_kwargs.id, str)
        self.assertEqual(self.instance_with_kwargs.id, self.instance_with_kwargs.id)
        self.assertIsInstance(self.instance_with_kwargs.created_at, datetime)
        self.assertIsInstance(self.instance_with_kwargs.updated_at, datetime)

    def test_save(self):
        """
        Test the save method of the BaseModel
        """
        old_updated_at = self.instance.updated_at
        self.instance.save()
        self.assertNotEqual(self.instance.updated_at, old_updated_at)

    def test_to_dict(self):
        """
        Test the to_dict method of the BaseModel
        """
        instance_dict = self.instance.to_dict()
        self.assertEqual(instance_dict["__class__"], "BaseModel")
        self.assertEqual(instance_dict["id"], self.instance.id)
        self.assertEqual(instance_dict["created_at"], self.instance.created_at.isoformat())
        self.assertEqual(instance_dict["updated_at"], self.instance.updated_at.isoformat())

    def test_str(self):
        """
        Test the __str__ method of the BaseModel
        """
        string_rep = str(self.instance)
        expected_string = f"[{self.instance.__class__.__name__}] ({self.instance.id}) {self.instance.__dict__}"
        self.assertEqual(string_rep, expected_string)

if __name__ == "__main__":
    unittest.main()
