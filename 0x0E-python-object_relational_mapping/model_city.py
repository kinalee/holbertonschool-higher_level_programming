#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import State, Base
"""
City Model
"""


class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer, autoincrement=True, nullable=False,
                primary_key=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
