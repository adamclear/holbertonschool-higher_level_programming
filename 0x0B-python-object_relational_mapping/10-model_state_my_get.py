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

    try:
        print(dbsession().query(State).filter(
            State.name == argv[4])[0].id)

    except Exception:
        print("Not Found")

    dbsession().close
