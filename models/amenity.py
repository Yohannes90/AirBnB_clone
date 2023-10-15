#!/usr/bin/python3
"""Amenity class module, this class will inherit from base model
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents amenity for app or console

        Attributes:
            name (str): name of amenity.
    """
    name = ""
