#!/usr/bin/python3
"""Place class module, this class will inherit from base model
"""
from models.base_model import BaseModel

class Place(BaseModel):
    """Represents place for app or console

        Attributes:
            city_id (str): City.id
            user_id (str): User.id
            name (str): name of place
            description (str): description of place
            number_rooms (integer): number of rooms in place
            number_bath_rooms (integer): number of bath rooms in place
            max_guest (integer): max capacity og guests
            price_by_night (integer): price by night
            latitude (float): latitude of place
            longitude (float): longtude of place
            amenity_ids (list): the list of Amenity.id
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bath_rooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """Instantiates new place

            Args:
                args: array of values to set inst attrs (not in use)
                kwargs: key value pairs to assign to instance
        """
        super().__init__(self, *args, **kwargs)
