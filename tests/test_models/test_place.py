#!/usr/bin/python3
"""Module that contains unittests for models/place.py"""
from models.place import Place
from tests.test_models.test_base_model import test_baseModel


class test_place(test_baseModel):
    """Defines unit tests for models/place.py"""

    def __init__(self, *args, **kwargs):
        """initalize place instance"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """checks city id is str"""
        new_place = self.value()
        self.assertIsInstance(new_place.city_id, str)

    def test_user_id(self):
        """checks user id is str"""
        new_place = self.value()
        self.assertIsInstance(new_place.user_id, str)

    def test_place_name(self):
        """checks place name is str"""
        new_place = self.value()
        self.assertIsInstance(new_place.name, str)

    def test_description(self):
        """checks description is str"""
        new_place = self.value()
        self.assertIsInstance(new_place.description, str)

    def test_number_rooms(self):
        """checks number rooms is int"""
        new_place = self.value()
        self.assertIsInstance(new_place.number_rooms, int)

    def test_number_bathrooms(self):
        """checks number bathrooms is int"""
        new_place = self.value()
        self.assertIsInstance(new_place.number_bathrooms, int)

    def test_max_guest(self):
        """checks max guest is int"""
        new_place = self.value()
        self.assertIsInstance(new_place.max_guest, int)

    def test_price_by_night(self):
        """checks price by night is int"""
        new_place = self.value()
        self.assertIsInstance(new_place.price_by_night, int)

    def test_latitude(self):
        """checks latitude is float"""
        new_place = self.value()
        self.assertIsInstance(new_place.latitude, float)

    def test_longitude(self):
        """checks longitude is float"""
        new_place = self.value()
        self.assertIsInstance(new_place.longitude, float)

    def test_amenity_ids(self):
        """checks amenity_ids is list"""
        new_place = self.value()
        self.assertIsInstance(new_place.amenity_ids, list)
