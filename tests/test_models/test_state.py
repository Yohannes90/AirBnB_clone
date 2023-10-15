#!/usr/bin/python3
"""Module that contains unittests for models/state.py"""
from models.state import State
from tests.test_models.test_base_model import test_baseModel


class test_state(test_baseModel):
    """Defines unit tests for models/state.py"""

    def __init__(self, *args, **kwargs):
        """initalize state instance"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_state_name(self):
        """checks state name is str"""
        new_state = self.value()
        self.assertIsInstance(new_state.name, str)
