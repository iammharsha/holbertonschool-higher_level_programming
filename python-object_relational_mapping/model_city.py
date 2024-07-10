#!/usr/bin/python3
"""Module for Class City"""
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """Definition of SQL table cities"""
    __tablename__ = "cities"
    id = Column(
            Integer,
            primary_key=True,
            autoincrement=True,
            nullable=False,
            unique=True
        )
    name = Column(String(128))
    state_id = Column(
                Integer,
                ForeignKey('states.id'),
                nullable=False
            )
