#!/usr/bin/python3
"""A class that stores Amenity inherited from BaseModel"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """A class that stores amenity information for HBnB listings"""

    name = ""
    count = 0
