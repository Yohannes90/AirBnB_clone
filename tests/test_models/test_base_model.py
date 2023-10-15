#!/usr/bin/python3
"""Module that contains unittests for models/base_model.py"""
import datetime
import json
from models.base_model import BaseModel
import os
import unittest
from uuid import UUID


class test_baseModel(unittest.TestCase):
    """Defines unittests for models/base_model.py
    """

    def __init__(self, *args, **kwargs):
        """initalize instance"""
        super().__init__(*args, *kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def test_default(self):
        """checks defalt instantiation"""
        bm = self.value()
        self.assertIsInstance(bm, self.value)

    def test_kwargs(self):
        """checks two instances with same kwargs are not same instances"""
        bm = self.value()
        copy = bm.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is bm)

    def test_kwargs_int(self):
        """checks kwargs with int arguments"""
        bm = self.value()
        copy = bm.to_dict()
        copy.update({1 : 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_kwargs_none(self):
        """checks kwargs with none arguments"""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = BaseModel(**n)

    def test_id(self):
        """checks id is string"""
        bm = self.value()
        self.assertIsInstance(bm.id, str)

    def test_created_at(self):
        """checks created_at is type datetime"""
        bm = self.value()
        self.assertIsInstance(bm.created_at, datetime.datetime)

    def test_updated_at(self):
        """checks updated_at is type datetime, not biased when given date as key"""
        bm = self.value()
        self.assertIsInstance(bm.updated_at, datetime.datetime)
        n = bm.to_dict()
        bm = BaseModel(**n)
        self.assertFalse(bm.created_at == bm.updated_at)

    def test_to_str(self):
        """checks __str__ returns desired output"""
        bm = self.value()
        self.assertEqual(str(bm), '[{}] ({}) {}'.format(self.name, bm.id, bm.__dict__))

    def test_todict(self):
        """check to_dict method"""
        bm = self.value()
        new = bm.to_dict()
        self.assertEqual(bm.to_dict(), new)

    def test_save(self):
        """ check save is storing same data as we get from dict"""
        bm = self.value()
        bm.save()
        key = "BaseModel." + bm.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], bm.to_dict())

    def setup(self):
        """define instructions that will be excuted before each test methods"""
        try:
            os.rename('file.json', "tmp")
        except IOError:
            pass

    def teardown(self):
        """define instructions that will be excuted after each test methods"""
        try:
            os.remove('file.json')
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
