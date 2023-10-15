#!/usr/bin/python3
"""User class module, this class will inherit from base model
"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class to manage users for app or console

        Attributes:
            email (str): user email initially empty
            password (str): user password initially empty
            first_name (str): user first name initially empty
            last_name (str): user last name initally empty
    """

    email = ''
    password = ''
    first_name = ''
    last_name = ''
