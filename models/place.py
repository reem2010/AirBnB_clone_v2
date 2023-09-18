#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, Float, ForeignKey, String, Integer, Table
from sqlalchemy.orm import relationship
import os


place_amenity = Table(
        "place_amenity",
        Base.metadata,
        Column(
            "place_id", String(60), ForeignKey("places.id"), nullable=False),
        Column(
            "amenity_id", String(60),
            ForeignKey("amenities.id"), nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if os.environ.get("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship(
            "Review", cascade="all, delete, delete-orphan", backref="place")
        amenities = relationship(
                "Amenity", secondary=place_amenity,
                viewonly=False, backref="place_amenities")
    else:
        @property
        def reviews(self):
            """returns the list of Review instances
            with place_id equals to the current Place.id"""

            all_reviews = models.storage.all("Review")
            result = []

            for key, value in all_reviews.items():
                if value.place_id == self.id:
                    result.append(value)
            return result
