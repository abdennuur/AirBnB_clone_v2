#!/usr/bin/python3
"""define City class"""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship
from sqlalchemy import Integer


class City(BaseModel, Base):
    """Represent city for MySQL database

    Inherits frm SQLAlchemy Base and links to MySQL table cities.

    Attributes:
        __tablename__ (str): name of MySQL table to store Cities.
        name (sqlalchemy String): name of City.
        state_id (sqlalchemy String): state id of City.
    """
    __tablename__ = "cities"
    id = Column(String(60), primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    places = relationship("Place", backref="cities", cascade="delete")
