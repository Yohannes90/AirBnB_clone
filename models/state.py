#!/usr/bin/python3
"""State class module, this class will inherit from base model
"""
from models.base_model import BaseModel

class State(BaseModel):
    """Represent states for app or console

        Attributes:
            name (str): name of state.
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """Instantiates new state

            Args:
                args: array of values to set inst attrs (not in use)
                kwargs: key value pairs to assign to instance
        """
        super().__init__(self, *args, **kwargs)
