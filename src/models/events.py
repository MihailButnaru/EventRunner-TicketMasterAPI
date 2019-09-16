# Copyright 2019 by Mihail Butnaru
# All rights reserved.
""" Mapped class that is used to create the Event table, which will store records
for the end-users using the application."""
from src.models import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Event(Base):
    """ Event table """
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    name = Column(String(150))
    type = Column(String(50))
    url = Column(String(1024))
    locale = Column(String(50))
    venues = relationship('Venue', back_populates='events')
    attractions = relationship('Attraction', back_populates='events')
