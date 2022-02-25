#!/usr/bin/python3
"""
This module contains the class: City
"""
from sqlalchemy import Column, ForeignKey, Integer, String
from model_state import Base


class City(Base):
    """
    This is the class: City
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
