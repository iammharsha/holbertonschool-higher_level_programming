#!/usr/bin/python3
"""Module to list all states and cities"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
                'mysql+mysqldb://{}:{}@localhost/{}'.format(
                    sys.argv[1], sys.argv[2], sys.argv[3]
                ),
                pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).\
            outerjoin(City).\
            order_by(State.id, City.id).\
            all():
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

    session.close()
