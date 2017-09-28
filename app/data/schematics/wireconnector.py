'''

A wire has two wire connectors, one at each end. These connectors
may be attached to another connector by a connection. If connection is
None, the wire connector is unattached.

'''

import uuid

from .schematicsconnector import SchematicsConnector
from data.util import Vector2i

class WireConnector(SchematicsConnector):
    def __init__(self, wire, pos = Vector2i()):
        super().__init__(wire)
        self.uuid = uuid.uuid1()

        self.wire = wire
        self.pos = pos
