#!/usr/bin/python3
"""
Uses SQLAlchemy to print state objects
"""

from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    Session = sessionmaker()
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (argv[1], argv[2], argv[3]), pool_pre_ping=True)
    session = Session(bind=engine)
    Base.metadata.create_all(engine)
    result = State(name="Louisiana")
    session.add(result)
    session.commit()
    result1 = session.query(State).filter_by(name="Louisiana").first()
    print(result1.id)
