#!/usr/bin/python3
"""Module to delete all states with letter a in table states"""
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
            all():
        session.delete(instance)

    session.commit()

    session.close()
