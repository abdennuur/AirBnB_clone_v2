#!/usr/bin/python3
"""To define Amenity class"""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Represent Amenity for MySQL database.

    Inherits frm SQLAlchemy Base and links to MySQL table amenities.

    Attributes:
        __tablename__ (str): name of MySQL table to store Amenities.
        name (sqlalchemy String): amenity name.
        place_amenities (sqlalchemy relationship): the Place-Amenity relationship.
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity",
                                   viewonly=False)
