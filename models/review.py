#!/usr/bin/python3
"""THIS MODULE CREATES A REVIEW CLASSES"""

from models.base_model import BaseModel


class Review(BaseModel):
    """THIS IS THE CLASSES FOR MANAGING REVIEW OBJECTS"""

    place_id = ""
    user_id = ""
    text = ""
