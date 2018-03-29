#!/usr/bin/python3
"""
Lists all state objects
"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from model_state import State, Base
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker()
    session = Session(bind=engine)
    Base.metadata.create_all(engine)
    result = session.query(State).filter
    (State.name.like('%a%')).order_by(State.id).all()
    if result:
        for x in result:
            print("{}: {}".format(result.id, result.name))
