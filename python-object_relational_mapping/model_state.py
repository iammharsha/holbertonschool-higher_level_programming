#!/usr/bin/python3
"""Module for State definition"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class which inherits from Base in SQLAlchemy"""
    __tablename__ = 'states'
    id = Column(
            Integer,
            primary_key=True,
            autoincrement=True,
            nullable=False,
            unique=True
        )
    name = Column(String(128))
