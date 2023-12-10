#!/usr/bin/python3
"""This script is THE base model"""

import uuid
from datetime import datetime
from models import storage



class BaseModel:

    """Base class for Inheritance across the system's classes."""

    def __init__(self, *args, **kwargs):
        """Initialize Instance attributes with flexible argument handling.

        Args:
            - *args: list Arguments
            - **kwargs: dict Key-values arguments
        """

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Get THE officialS SString representation."""

        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """update THE publicS instance attributeS updated_at"""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Convert THE object'S attributeS to a dictionary._"""

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
