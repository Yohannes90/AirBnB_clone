#!/usr/bin/python3
"""City class module, this class will inherit from base model
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Represent cities for app or console

        Attributes:
            state_id (str): State.id
            name (str): name of city.
    """
    state_id = ""
    name = ""
