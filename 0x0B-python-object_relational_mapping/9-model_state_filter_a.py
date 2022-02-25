#!/usr/bin/python3
"""
This script lists the State objects from the DB hbtn_0e_6_usa
that contain the letter 'a' in their name.
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    dbengine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                             .format(argv[1], argv[2], argv[3]),
                             pool_pre_ping=True)

    Base.metadata.create_all(dbengine)
    dbsession = sessionmaker(bind=dbengine)

    astates = dbsession().query(State).order_by(State.id)\
        .filter(State.name.like("%a%"))

    for row in astates:
        print("{}: {}".format(row.id, row.name))

    dbsession().close
