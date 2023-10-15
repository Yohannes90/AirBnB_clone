#!/usr/bin/python3
"""Module that contains unittests for models/amenity.py"""
from models.amenity import Amenity
from tests.test_models.test_base_model import test_baseModel


class test_amenity(test_baseModel):
    """Defines unit tests for models/amenity.py"""

    def __init__(self, *args, **kwargs):
        """initalize amenity instance"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_amenity_name(self):
        """checks amenity name is str"""
        new_amenity = self.value()
        self.assertIsInstance(new_amenity.name, str)
