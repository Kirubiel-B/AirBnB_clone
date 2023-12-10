#!/usr/bin/python3
"""THIS MODULE CREATES A USER CLASS"""

from models.base_model import BaseModel


class User(BaseModel):
    """THIS IS THE CLASS FOR managING userS ObjectS"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
