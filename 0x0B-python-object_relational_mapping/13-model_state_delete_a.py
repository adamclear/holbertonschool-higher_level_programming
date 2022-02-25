#!/usr/bin/python3
"""
This script deletes all State objects with the letter 'a'
in their name in DB hbtn_0e_6_usa.
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
    dbs = dbsession()

    deletem = dbs.query(State).filter(State.name.like('%a%'))
    for row in deletem:
        dbs.delete(row)
    dbs.commit()

    dbsession().close
