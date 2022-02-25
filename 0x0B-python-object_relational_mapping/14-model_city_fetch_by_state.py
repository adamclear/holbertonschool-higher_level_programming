#!/usr/bin/python3
"""
This script lists all City objects from the DB hbtn_0e_14_usa.
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    dbengine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                             .format(argv[1], argv[2], argv[3]),
                             pool_pre_ping=True)

    Base.metadata.create_all(dbengine)
    dbsession = sessionmaker(bind=dbengine)
    dbs = dbsession()

    findcities = dbs.query(State, City).filter(
        State.id == City.state_id).all()
    for state_item, city_item in findcities:
        print("{}: ({}) {}".format(state_item.name,
              city_item.id, city_item.name))

    dbsession().close
