#!/usr/bin/python3
"""Module that contains unittests for models/city.py"""
from models.city import City
from tests.test_models.test_base_model import test_baseModel


class test_city(test_baseModel):
    """Defines unit tests for models/city.py"""

    def __init__(self, *args, **kwargs):
        """instantiate city instance"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """checks state id is str"""
        new_city = self.value()
        self.assertIsInstance(new_city.state_id, str)

    def test_city_name(self):
        """checks city name is str"""
        new_city = self.value()
        self.assertIsInstance(new_city.name, str)
