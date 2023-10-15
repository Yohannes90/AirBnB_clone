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
