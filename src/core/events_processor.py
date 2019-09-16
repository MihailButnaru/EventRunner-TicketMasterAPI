# Copyright 2019 by Mihail Butnaru
# All rights reserved.
from src.models import session_scope
from src.models.events import Event
from src.models.venues import Venue
from src.models.attractions import Attraction
from src.models import events, attractions, venues

class EventProcessor():

    def __init__(self, api_data):
        self._api_data = api_data
        self._process = self.process()

    def process(self):
        """ Data is saved into the database """
        with session_scope() as session:
            self._event_data_session(session)
            self._venues_data_session(session)
            self._attractions_data_session(session)
            session.commit()

    def _event_data_session(self, session):
        """ Events data saves into db """
        events = self._api_data.event()
        for event in events:
            even = Event(**event)
            session.add(Event(**event))
        
    def _venues_data_session(self, session):
        """ Venues data session db """
        venues = self._api_data.event_venue()
        for venue in venues:
            session.add(Venue(**venue))

    def _attractions_data_session(self, session):
        """" Attractions data session db """
        attractions = self._api_data.event_attraction()
        for attraction in attractions:
            session.add(Attraction(**attraction))
