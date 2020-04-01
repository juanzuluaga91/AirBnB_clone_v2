#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Float, Integer
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from os import environ
import models
from sqlalchemy import Table, Text


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """

    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    if 'HBNB_TYPE_STORAGE' in environ and environ['HBNB_TYPE_STORAGE'] == 'db':
        reviews = relationship('Review', cascade="all, delete",
                               backref='place')
        amenities = relationship('Amenity',
                                 secondary="place_amenity",
                                 back_populates='place_amenities',
                                 viewonly=False)
    else:
        tmp_list = []

        @property
        def reviews(self):
            """"""

            for k, v in models.storage.items():
                if "Review" in k and v.place_id == self.id:
                    tmp_list.append(v)
            return tmp_list

        @property
        def amenities(self):
            """"""
            for k, v in models.storage.all().items():
                if "Amenity" in k and v.amenity_ids == self.id:
                    tmp_list.append(v)
            return tmp_list

        @amenities.setter
        def amenities(self, value):
            """"""
            if value.__class__.__name__ == "Amenity":
                self.amenity_ids.append(str(value.id))
