#!/usr/bin/python3

"""
Unittest BaseModel:
test_init
test_save
test_to_dict
"""


import unittest
from datetime import datetime
import uuid
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """
        Sets up the test methods
        """
        self.instance = BaseModel()
        self.instance_with_kwargs = BaseModel(id=str(uuid.uuid4()), created_at=datetime.today().isoformat(), updated_at=datetime.today().isoformat())

    def tearDown(self):
        """
        Clean up after test
        """
        del self.instance
        del self.instance_with_kwargs

    def test_instance_creation(self):
        """
        Test creation of a new instance of BaseModel
        """
        self.assertIsInstance(self.instance, BaseModel)
        self.assertIsInstance(self.instance.id, str)
        self.assertIsInstance(self.instance.created_at, datetime)
        self.assertIsInstance(self.instance.updated_at, datetime)

    def test_instance_creation_with_kwargs(self):
        """
        Test creation of a new instance of BaseModel with kwargs
        """
        self.assertIsInstance(self.instance_with_kwargs, BaseModel)
        self.assertIsInstance(self.instance_with_kwargs.id, str)
        self.assertEqual(self.instance_with_kwargs.id, self.instance_with_kwargs.id)
        self.assertIsInstance(self.instance_with_kwargs.created_at, datetime)
        self.assertIsInstance(self.instance_with_kwargs.updated_at, datetime)

    def test_save_method(self):
        """
        Test the save method of the BaseModel
        """
        old_updated_at = self.instance.updated_at
        self.instance.save()
        self.assertNotEqual(self.instance.updated_at, old_updated_at)

    def test_to_dict_method(self):
        """
        Test the to_dict method of the BaseModel
        """
        instance_dict = self.instance.to_dict()
        self.assertEqual(instance_dict["__class__"], "BaseModel")
        self.assertEqual(instance_dict["id"], self.instance.id)
        self.assertEqual(instance_dict["created_at"], self.instance.created_at.isoformat())
        self.assertEqual(instance_dict["updated_at"], self.instance.updated_at.isoformat())

    def test_str_method(self):
        """
        Test the __str__ method of the BaseModel
        """
        string_rep = str(self.instance)
        expected_string = f"[BaseModel] ({self.instance.id}) {self.instance.__dict__}"
        self.assertEqual(string_rep, expected_string)

if __name__ == "__main__":
    unittest.main()
