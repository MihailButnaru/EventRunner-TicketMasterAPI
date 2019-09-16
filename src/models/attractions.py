# Copyright 2019 by Mihail Butnaru
# All rights reserved.
""" Mapped class that is used to create the Attractions table, which will store records
for the end-users using the application."""
from src.models import Base
from src.models.events import Event
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String


class Attraction(Base):
    """ Attraction table """
    __tablename__ = 'attractions'

    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    type = Column(String(50), nullable=False)
    event_id = Column(Integer, ForeignKey(Event.id))
    events = relationship(Event, back_populates='attractions')
