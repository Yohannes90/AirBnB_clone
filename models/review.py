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

    def __init__(self, *args, **kwargs):
        """Instantiates new review

            Args:
                args: array of values to set inst attrs (not in use)
                kwargs: key value pairs to assign to instance
        """
        super().__init__(self, *args, **kwargs)
