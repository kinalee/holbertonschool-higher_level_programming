#!/usr/bin/python3
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
"""
First state model
"""

Base = declarative_base():

class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, nullable=False,
                primary_key=True, unique=True)
    name = Column(String(128), nullabe=False)
