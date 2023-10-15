#!/usr/bin/python3
"""Review class module, this class will inherit from base model
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents review for app or console

        Attributes:
            place_id (str): Place.id
            user_id (str): User.id
            text (str): text of review
    """
    place_id = ""
    user_id = ""
    text = ""
