#!/usr/bin/python3
"""
Lists all state objects
"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from model_state import State, Base
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    for instance in session.query(State).order_by(State.id):
        print("{}: {}".format(instance.id, instance.name))
