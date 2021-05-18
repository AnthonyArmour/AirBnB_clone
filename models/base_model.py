#!/usr/bin/python3
"""
This is the class BaseModel which defines all attributes
for the classes in AirBnb project
"""

from datetime import datetime
import uuid
from models import storage


class BaseModel():

    """defines all attributes and methods of clases"""

    count = 0
    created_at = ""
    updated_at = ""
    id = ""

    def __init__(self, *args, **kwargs):
        if not kwargs or len(kwargs) == 0:
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            self.id = str(uuid.uuid4())
            storage.new(self)
        else:
            for k in kwargs:
                if k == "__class__":
                    continue
                if k == "created_at" or k == "updated_at":
                    obj = datetime.strptime(kwargs[k], '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, k, obj)
                    continue
                setattr(self, k, kwargs[k])
        BaseModel.count += 1

    def save(self):
        """updates instance attribute update_at"""
        self.updated_at = datetime.today()
        storage.save()

    def to_dict(self):
        """returns dictionary of instance attributes"""
        dic = self.__dict__.copy()
        dic["__class__"] = BaseModel.__name__
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        return dic

    def __del__(self):
        """Decrements count on instance deletion"""
        BaseModel.count -= 1

    def __str__(self):
        """returns printable string of object"""
        st = "[{}] ({}) {}".format(BaseModel.__name__, self.id, self.__dict__)
        return st
