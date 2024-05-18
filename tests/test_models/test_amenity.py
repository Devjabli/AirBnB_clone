#!/usr/bin/python3
"""
Module Amenity class
"""
import os
import unittest
import uuid
from datetime import datetime
from time import sleep
from models.amenity import Amenity
import models


class TestAmenityInstantiation(unittest.TestCase):
    """Tests for Amenity class instantiation"""

    def test_instantiation(self):
        u = Amenity()
        self.assertIsInstance(u, Amenity)
        self.assertIn(u, models.storage.all().values())
        self.assertIsInstance(u.id, str)
        self.assertIsInstance(u.created_at, datetime)
        self.assertIsInstance(u.updated_at, datetime)
        self.assertTrue(hasattr(u, "name"))
    
    def test_unique_ids(self):
        u1, u2 = Amenity(), Amenity()
        self.assertNotEqual(u1.id, u2.id)

    def test_str_representation(self):
        u = Amenity()
        u.id = str(uuid.uuid4())
        u.created_at = u.updated_at = datetime.now()
        str_repr = str(u)
        self.assertIn("[Amenity]", str_repr)