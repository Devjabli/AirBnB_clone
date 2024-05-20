#!/usr/bin/python3
"""
Module for User class
"""
import os
import unittest
from datetime import datetime
from time import sleep
from models.user import User
import models


class TestUserInstantiation(unittest.TestCase):
    """Tests for User class instantiation"""

    def test_instantiation(self):
        u = User()
        self.assertIsInstance(u, User)
        self.assertIn(u, models.storage.all().values())
        self.assertIsInstance(u.id, str)
        self.assertIsInstance(u.created_at, datetime)
        self.assertIsInstance(u.updated_at, datetime)
        self.assertTrue(hasattr(u, "email"))
        self.assertTrue(hasattr(u, "password"))
        self.assertTrue(hasattr(u, "first_name"))
        self.assertTrue(hasattr(u, "last_name"))

    def test_unique_ids(self):
        u1, u2 = User(), User()
        self.assertNotEqual(u1.id, u2.id)

    def test_different_timestamps(self):
        u1 = User()
        sleep(0.05)
        u2 = User()
        self.assertNotEqual(u1.created_at, u2.created_at)
        self.assertNotEqual(u1.updated_at, u2.updated_at)

    def test_str_representation(self):
        u = User()
        u.id = "123456"
        u.created_at = u.updated_at = datetime.today()
        str_repr = str(u)
        self.assertIn("[User] (123456)", str_repr)
        self.assertIn("'id': '123456'", str_repr)

    def test_kwargs_instantiation(self):
        dt = datetime.now().isoformat()
        u = User(id="123", created_at=dt, updated_at=dt)
        self.assertEqual(u.id, "123")
        self.assertEqual(u.created_at.isoformat(), dt)
        self.assertEqual(u.updated_at.isoformat(), dt)


class TestUserSave(unittest.TestCase):
    """Tests for User class save method"""

    def setUp(self):
        self.filename = "file.json"
        if os.path.exists(self.filename):
            os.rename(self.filename, "tmp")

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)
        if os.path.exists("tmp"):
            os.rename("tmp", self.filename)

    def test_save_updates_timestamp(self):
        u = User()
        old_updated_at = u.updated_at
        sleep(0.05)
        u.save()
        self.assertNotEqual(old_updated_at, u.updated_at)

    def test_save_updates_file(self):
        u = User()
        u.save()
        with open(self.filename, "r") as f:
            self.assertIn(f"User.{u.id}", f.read())


class TestUserToDict(unittest.TestCase):
    """Tests for User class to_dict method"""

    def test_to_dict_output(self):
        u = User()
        u_dict = u.to_dict()
        self.assertIsInstance(u_dict, dict)
        self.assertIn("id", u_dict)
        self.assertIn("created_at", u_dict)
        self.assertIn("updated_at", u_dict)
        self.assertIn("__class__", u_dict)

    def test_to_dict_contains_correct_types(self):
        u = User()
        u_dict = u.to_dict()
        self.assertIsInstance(u_dict["id"], str)
        self.assertIsInstance(u_dict["created_at"], str)
        self.assertIsInstance(u_dict["updated_at"], str)

    def test_to_dict_added_attributes(self):
        u = User()
        u.middle_name = "Aroussi"
        u.my_number = 64
        u_dict = u.to_dict()
        self.assertEqual(u_dict["middle_name"], "Aroussi")
        self.assertEqual(u_dict["my_number"], 64)

class TestUserAttributes(unittest.TestCase):
    """Tests for User class attributes"""

    def test_email(self):
        """Test if string"""
        user = User()
        self.assertIsInstance(user.email, str)

    def test_password(self):
        """Test if string"""
        user = User()
        self.assertIsInstance(user.password, str)

    def test_first_name(self):
        """Test if string"""
        user = User()
        self.assertIsInstance(user.first_name, str)

    def test_last_name(self):
        """Test if string"""
        user = User()
        self.assertIsInstance(user.last_name, str)


if __name__ == '__main__':
    unittest.main()
