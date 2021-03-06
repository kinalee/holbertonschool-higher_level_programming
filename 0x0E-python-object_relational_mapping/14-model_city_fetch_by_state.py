#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    for data in session.query(City, State).filter(City.state_id ==
                                                  State.id).order_by(City.id):
        print("{:s}: ({:d}) {:s}"
              .format(data.State.name, data.City.id, data.City.name))
