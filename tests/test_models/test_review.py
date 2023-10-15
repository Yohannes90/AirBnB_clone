#!/usr/bin/python3
"""Module that contains unittests for models/review.py"""
from models.review import Review
from tests.test_models.test_base_model import test_baseModel


class test_review(test_baseModel):
    """Defines unit tests for models/review.py"""

    def __init__(self, *args, **kwargs):
        """initalize review instance"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """checks place id is str"""
        new_review = self.value()
        self.assertIsInstance(new_review.place_id, str)

    def test_user_id(self):
        """checks user id is str"""
        new_review = self.value()
        self.assertIsInstance(new_review.user_id, str)

    def test_text(self):
        """checks review text is str"""
        new_review = self.value()
        self.assertIsInstance(new_review.text, str)
