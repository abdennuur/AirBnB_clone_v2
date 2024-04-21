#!/usr/bin/python3
"""Define State class"""
import models
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.city import City
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """Represent state for MySQL database.

    Inherits frm SQLAlchemy Base and links to MySQL table states

    Attributes:
        __tablename__ (str): name of MySQL table to store States.
        name (sqlalchemy String): name of State.
        cities (sqlalchemy relationship): State-City relationship.
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City",  backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE", "fs") != "db":
        @property
        def cities(self):
            """Get list of all related City objcts"""
            city_ls = []
            for ct in list(models.storage.all(City).values()):
                if ct.state_id == self.id:
                    city_ls.append(ct)
            return city_ls
