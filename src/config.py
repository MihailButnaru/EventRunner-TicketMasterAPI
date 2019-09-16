# Copyright 2019 by Mihail Butnaru
# All rights reserved.
""" Configuration that holds the settings of the application """
import os

class Config:

    #### TICKET MASTER CONFIGURATION ####
    @property
    def TICKET_MASTER_API_KEY(self):
        """ """
        return os.getenv('TICKET_MASTER_API_KEY', 'ZgRIqVFQJNHl9nM4DT8DzLXMmXCWPG1A')

    @property
    def TICKET_MASTER_ENDPOINT(self):
        """ """
        return os.getenv('TICKET_MASTER_ENDPOINT', 'https://app.ticketmaster.com/discovery/v2/events.json?')


    #### POSTGRES CONFIGURATIONS
    @property
    def DATABASE_CONNECTION(self):
        """ """
        return os.getenv('DATABASE_NAME', 'postgresql+psycopg2://postgres:postgres@localhost/ticketmaster')
