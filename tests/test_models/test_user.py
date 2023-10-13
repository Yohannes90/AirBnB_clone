#!/usr/bin/python3
"""Module that contains unittests for models/user.py"""
from test_base_model import test_basemodel
from models.user import User

class test_user(test_basemodel):
    """Defines unit tests for models/user.py"""
    def test_first_name(self):
        """check type of first_name is string"""
        new = User()
        self.assertIsInstance(new.first_name, str)

    def test_last_name(self):
        """check type of last_name is string"""
        new = User()
        self.assertIsInstance(new.last_name, str)

    def test_email(self):
        """check type of email is string"""
        new = User()
        self.assertIsInstance(new.email, str)

    def test_password(self):
        """check type of password is string"""
        new = User()
        self.assertIsInstance(new.password, str)
