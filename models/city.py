#!/usr/bin/python3
"""THIS MODULE CREATES A USER CLASS"""

from models.base_model import BaseModel


class City(BaseModel):
    """This IS THE class FOR managing CITY objects"""

    state_id = ""
    name = ""
