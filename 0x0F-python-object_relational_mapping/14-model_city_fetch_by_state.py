#!/usr/bin/python3
"""
Uses SQLAlchemy to print state objects
"""

from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
from model_city import City

if __name__ == "__main__":
    Session = sessionmaker()
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (argv[1], argv[2], argv[3]), pool_pre_ping=True)
    session = Session(bind=engine)
    Base.metadata.create_all(engine)
    result = session.query(State, City).filter(City.state_id == State.id).all()
    for obj in result:
        print("{}: ({}) {}".format(obj[0].name, obj[1].id, obj[1].name))
