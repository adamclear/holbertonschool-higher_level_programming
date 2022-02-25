#!/usr/bin/python3
"""
This script changes the name of the State object with the
id '2', to 'New Mexico'.
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

    upstate = dbs.query(State).filter(State.id == 2).one()
    upstate.name = "New Mexico"
    dbs.commit()

    dbsession().close
