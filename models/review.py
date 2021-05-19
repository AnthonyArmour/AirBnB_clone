#!/usr/bin/python3
"""A module that stores Review inherited from BaseModel"""


from models.base_model import BaseModel


class Review(BaseModel):
    """A class that stores reviews of HBnB listings"""

    place_id = ""
    user_id = ""
    text = ""
    count = 0
