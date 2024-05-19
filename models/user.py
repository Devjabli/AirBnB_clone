#!/usr/bin/python3
"""
Module for the User class.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    class User information data
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
