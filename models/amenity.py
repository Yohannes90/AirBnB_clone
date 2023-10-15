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

    def __init__(self, *args, **kwargs):
        """Instantiates new amenity

            Args:
                args: array of values to set inst attrs (not in use)
                kwargs: key value pairs to assign to instance
        """
        super().__init__(self, *args, **kwargs)
