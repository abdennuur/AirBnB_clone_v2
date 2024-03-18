#!/usr/bin/python3
"""define BaseModel class"""
import models
from uuid import uuid4
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import String

Base = declarative_base()


class BaseModel:
    """defines BaseModel class.

    Attributes:
        id (sqlalchemy String): BaseModel id.
        created_at (sqlalchemy DateTime): datetime at creation.
        updated_at (sqlalchemy DateTime): datetime of last update.
    """

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """To initialize new BaseModel

        Args:
            *args (any): unused
            **kwargs (dict): Key/value attributes pairs
        """
        self.id = str(uuid4())
        self.created_at = self.updated_at = datetime.utcnow()
        if kwargs:
            for ky, val in kwargs.items():
                if ky == "created_at" or ky == "updated_at":
                    val = datetime.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")
                if ky != "__class__":
                    setattr(self, ky, val)

    def save(self):
        """To update updated_at with current datetime"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Return -> dictionary representation of BaseModel instance.

        Include key/value pair __class__ representing
        class name of object
        """
        my_dct = self.__dict__.copy()
        my_dct["__class__"] = str(type(self).__name__)
        my_dct["created_at"] = self.created_at.isoformat()
        my_dct["updated_at"] = self.updated_at.isoformat()
        my_dct.pop("_sa_instance_state", None)
        return my_dct

    def delete(self):
        """To delete current instance frm storage"""
        models.storage.delete(self)

    def __str__(self):
        """Return -> print/str representation of BaseModel instance"""
        dc = self.__dict__.copy()
        dc.pop("_sa_instance_state", None)
        return "[{}] ({}) {}".format(type(self).__name__, self.id, dc)
