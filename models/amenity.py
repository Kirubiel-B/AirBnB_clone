#!/usr/bin/python3
"""Define the Amenity class."""


from models.base_model import BaseModel



class Amenity(BaseModel):
    """Class representing amenities in the system.

    This class inherits from BaseModel and serves as a blueprint for creating
    Amenity objects. Each Amenity object may have a name attribute indicating
    the type of amenity it represents.
    """

    name = ""
