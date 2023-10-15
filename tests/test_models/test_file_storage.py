#!/usr/bin/python3
"""Unittests for file storage in this file"""
import unittest
from models import storage
from models.base_model import BaseModel
import os
import json


class test_file_storage(unittest.TestCase):
    """all tests to test file storage engine"""

    def test_all_return(self):
        """test that all returns a dictionary"""
        self.assertIsInstance(storage.all(), dict)

    def test_new_sets_obj(self):
        """test that new sets obj correctly in __objects"""
        bm = BaseModel()
        key = "BaseModel." + bm.id
        self.assertTrue(key in storage.all().keys())

    def test_save(self):
        """test that object is saved when instance is created"""
        bm = BaseModel()
        bm.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        """test whether reloads correct items"""
        bm = BaseModel()
        bm.save()
        with open("file.json", 'r') as f:
            j = json.load(f)
            storage.reload()
            self.assertEqual(j, storage.all())

    def tearDown(self):
        """remove file when finished"""
        if os.path.exists("file.json"):
            os.remove("file.json")


if __name__ == "__main__":
    unittest.main()
