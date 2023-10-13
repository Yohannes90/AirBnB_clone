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

    def test_default(self):
        """checks defalt instantiation"""
        bm = BaseModel()
        self.assertIsInstance(bm, BaseModel)

    def test_kwargs(self):
        """checks two instances with same kwargs are not same instances"""
        bm = BaseModel()
        copy = bm.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is bm)

    def test_kwargs_int(self):
        """checks kwargs with int arguments"""
        bm = BaseModel()
        copy = bm.to_dict()
        copy.update({1 : 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_kwargs_none(self):
        """checks kwargs with none arguments"""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = BaseModel(**n)

    # def test_kwargs_one(self):
    #     """checks kwargs with one correct argument"""
    #     n = {'Name': 'test'}
    #     with self.assertRaises(KeyError):
    #         new = BaseModel(**n)

    def test_id(self):
        """checks id is string"""
        new = BaseModel()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """checks created_at is type datetime"""
        new = BaseModel()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """checks updated_at is type datetime, not biased when given date as key"""
        new = BaseModel()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)

    def test_to_str(self):
        """checks __str__ returns desired output"""
        bm = BaseModel()
        self.assertEqual(str(bm), '[{}] ({}) {}'.format("BaseModel", bm.id, bm.__dict__))

    def test_todict(self):
        """check to_dict method"""
        bm = BaseModel()
        new = bm.to_dict()
        self.assertEqual(bm.to_dict(), new)

    # def test_save(self):
    #     """ check save is storing same data as we get from dict"""
    #     bm = BaseModel()
    #     bm.save()
    #     key = "BaseModel." + bm.id
    #     with open('file.json', 'r') as f:
    #         j = json.load(f)
    #         self.assertEqual(j[key], bm.to_dict())

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
