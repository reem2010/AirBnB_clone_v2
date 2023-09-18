#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
import os
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if os.environ.get("HBNB_TYPE_STORAGE") == "db":
        cities = relationship(
                "City", backref="state", cascade="all, delete-orphan")
    else:
        @property
        def cities(self):
            """returns the list of City instances"""
            res = []
            for value in models.storage.all(City).values():
                if value.state_id == self.id:
                    res.append(value)
            return res
