#!/usr/bin/python3
"""A module that stores City inherited from BaseModel"""


from models.base_model import BaseModel


class City(BaseModel):
    """A class that stores City information for BaseModel"""

    state_id = ""
    name = ""
    count = 0
