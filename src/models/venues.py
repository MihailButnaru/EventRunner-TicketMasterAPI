# Copyright 2019 by Mihail Butnaru
# All rights reserved.
""" Mapped class that is used to create the Venue table, which will store records
for the end-users using the application."""
from src.models import Base
from sqlalchemy import ForeignKey
from src.models.events import Event
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer


class Venue(Base):
    """ Venue table """
    __tablename__ = 'venues'

    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    type = Column(String(50), nullable=False)
    postcode = Column(String(100), nullable=False)
    address = Column(String(100), nullable=False)
    event_id = Column(Integer, ForeignKey(Event.id))
    events = relationship(Event, back_populates='venues')
