#!/usr/bin/python3
"""A module that holds User inherited from BaseModel"""


from models.base_model import BaseModel


class User(BaseModel):
    """A class that holds user information for hbnb instances"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
    count = 0
