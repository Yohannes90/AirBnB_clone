#!/usr/bin/python3
"""Module that contains unittests for models/user.py"""
from models.user import User
import unittest
from datetime import datetime
import uuid

class test_user(unittest.TestCase):
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

    def test_created_at(self):
        """check if created_at is assigned datetime object"""
        new = User()
        self.assertIsInstance(new.created_at, datetime)

    def test_updated_at(self):
        """check if updated at is assigned datetime object"""
        new = User()
        self.assertIsInstance(new.updated_at, datetime)

    def test_kwargs_asignment(self):
        """check if kwargs gest assigned to inst"""
        new1 = User()
        new1.name = "John"

        key_word_args = {"name" : "Betty", "surname" : "Battery", "age" : 98}
        new2 = User(**key_word_args)

        self.assertEqual(new1.name, "John")
        
        self.assertEqual(new2.name, "Betty")
        self.assertEqual(new2.surname, "Battery")
        self.assertEqual(new2.age, 98)

    def test_id_assignment(self):
        """check if id is assigned a uuid4 uuid"""
        new = User()
        tmp_id = uuid.uuid4()
        self.assertIsInstance(new.id, str)
