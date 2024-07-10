#!/usr/bin/python3
"""Module to list all states with letter a in db hbtn_0e_6_usa"""
import sys
from model_state import Base, State
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

    for instance in session.query(State).\
            filter(State.name.like('%a%')).\
            order_by(State.id):
        print("{}: {}".format(instance.id, instance.name))

    session.close()
