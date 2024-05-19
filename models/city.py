#!/usr/bin/python3
"""
Module City class.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Representing city.

    Attributes:
        state_id (str): The state id.
        name (str): name city.
    """

    state_id = ""
    name = ""
