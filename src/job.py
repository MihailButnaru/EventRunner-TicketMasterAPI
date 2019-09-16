# Copyright 2019 by Mihail Butnaru
# All rights reserved.
""" Job Runnner """
from src.config import Config
from src.core.events_manager import EventsManager
from src.core.events_processor import EventProcessor


class JobRunner():

    def __init__(self, country_code):
        self._config = Config()
        self._event_manager = EventsManager(self._config, country_code)
        self._processor = EventProcessor(self._event_manager)

    def runner(self):
        return self._processor
