#!/usr/bin/python3
"""
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv, environ
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classes = [Amenity, City, Place, Review, State, User]


class DBStorage():
    """
    """
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if 'HBNB_ENV' in environ and environ['HBNB_ENV'] == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """
        """
        new_dict = {}
        for c in classes:
            if cls is None or cls is classes[c] or cls is c:
                objs = self.__session.query(classes[c]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """
        """
        self.__session.add(obj)

    def save(self):
        """
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)()
