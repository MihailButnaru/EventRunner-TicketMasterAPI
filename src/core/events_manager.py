# Copyright 2019 by Mihail Butnaru
# All rights reserved.
""" Manager will handle the requests to the API to get the correct data """
import requests

class EventsManager():

    def __init__(self, config, country_code):
        self._config = config
        self._country_code = country_code
        self._events = self.get()

    def get(self):
        """ Returns the data from the API """
        params = {
            'countryCode': self._country_code, 
            'apikey' : self._config.TICKET_MASTER_API_KEY
                }
        response = requests.get(
                    self._config.TICKET_MASTER_ENDPOINT, params=params)
        return response.json()

    def event(self):
        """ Returns the events """
        events = []
        for event in self._events['_embedded']['events']:
            events.append({
                'name':event['name'],
                'type':event['type'],
                'url':event['url'],
                'locale':event['locale']
            })
        return events

    def event_venue(self):
        """ Returns the venues of the event """
        venues = []
        for event in self._events['_embedded']['events']:
            for venue in event['_embedded']['venues']:
                venues.append({
                    'name' : venue['name'],
                    'type' : venue['type'],
                    'postcode' : venue['postalCode'],
                    'address' : venue['address']['line1']
                })
        return venues
        
    def event_attraction(self):
        """ Returns the attractions of the event """
        attractions = []
        for event in self._events['_embedded']['events']:
            for attraction in event['_embedded']['attractions']:
                attractions.append({
                    'name' : attraction['name'],
                    'type' : attraction['type'],
                })
        return attractions
