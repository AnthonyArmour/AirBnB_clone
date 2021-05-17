#!/usr/bin/python3
"""
This is the class BaseModel which defines all attributes
for the classes in AirBnb project
"""

import datetime
import uuid


class BaseModel():

    """defines all attributes and methods of clases"""

    count = 0
    created_at = ""
    updated_at = ""
    id = ""

    def __init__(self):
        dateTime = datetime.datetime.today()
        self.created_at = dateTime.isoformat()
        self.updated_at = dateTime.isoformat()
        self.id = str(uuid.uuid4())
        BaseModel.count += 1

    def save(self):
        """updates instance attribute update_at"""
        dateTime = datetime.datetime.today()
        self.updated_at = dateTime.isoformat()

    def to_dict(self):
        """returns dictionary of instance attributes"""
        dic = self.__dict__.copy()
        dic["__class__"] = BaseModel.__name__
        return dic

    def __del__(self):
        """Decrements count on instance deletion"""
        BaseModel.count -= 1

    def __str__(self):
        """returns printable string of object"""
        st = "[{}] ({}) {}".format(BaseModel.__name__, self.id, self.__dict__)
        return st
