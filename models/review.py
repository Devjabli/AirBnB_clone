#!/usr/bin/python3
"""
Module Review class.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Representing review.

    Attributes:
        place_id (str): return string id.
        user_id (str): return string id.
        text (str): return string text.
    """

    place_id = ""
    user_id = ""
    text = ""
