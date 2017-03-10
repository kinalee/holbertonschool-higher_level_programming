#!/usr/bin/python3
from SQLAlchemy import *
"""
First state model
"""

Base = declarative_base():

class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, nullable=False,
                primary_key=True, unique=True)
    name = Column(String(128), nullabe=False)
