"""Uses python pickle to write logs to a blob file. Probably not helpful"""

from pickle import dump
from typing import Iterator

from nari.io.writer import Writer
from nari.types.event.base import Event

class PickleWriter(Writer):
    """Writes a stream of events into a binary file"""
    def __init__(self, stream: Iterator[Event], filename: str):
        super().__init__(stream)
        self.handle = open(filename, 'wb')

    def write_next(self, event: Event):
        dump(event, self.handle)
