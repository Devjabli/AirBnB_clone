#!/usr/bin/python3
"""
Module Place class.
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represent a place.

    Attributes:
        city_id (str): id.
        user_id (str): id.
        name (str): return name string.
        description (str): return name string.
        number_rooms (int): return number integer.
        number_bathrooms (int): return number integer.
        max_guest (int): return number max integer.
        price_by_night (int): return number integer.
        latitude (float): return number float.
        longitude (float): return number float.
        amenity_ids (list): A list of ids.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
