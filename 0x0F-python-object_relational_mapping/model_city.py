#!/usr/bin/python3
"""
Class City
"""

from model_state import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """
    city inherits from base
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
