import uuid

'''

A wire has two wire connectors, one at each end. These connectors
may be attached to another connector by a connection. If connection is
None, the wire connector is unattached.

'''

from .schematicsconnector import SchematicsConnector
from data.util import Vector2i

class WireConnector(SchematicsConnector):
    def __init__(self, wire, pos = Vector2i()):
        self.uuid = uuid.uuid1()
        
        self.wire = wire
        self.connection = None
        self.pos = pos